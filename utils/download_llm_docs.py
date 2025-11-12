#!/usr/bin/env python3
"""
Universal LLM Documentation Downloader - Async Version

This script downloads and saves documentation from llms.txt files
using async/await for high-performance parallel downloads.

llms.txt is a standard format for providing LLM-optimized documentation.

Usage:
    python download_llm_docs.py [URLs...]
    python download_llm_docs.py --config urls.txt
    python download_llm_docs.py --url https://docs.example.com/llms.txt
"""

import argparse
import asyncio
import json
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse

try:
    import aiohttp
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing required dependencies...")
    import subprocess

    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-q",
            "aiohttp",
            "beautifulsoup4",
            "lxml",
        ]
    )
    import aiohttp
    from bs4 import BeautifulSoup


class LLMDocsDownloader:
    """Downloads and organizes LLM documentation from llms.txt files."""

    def __init__(
        self,
        output_dir: str = "llm_docs",
        delay: float = 0.1,
        max_retries: int = 3,
        max_concurrent: int = 10,
        try_variants: bool = True,
    ):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.delay = delay
        self.max_retries = max_retries
        self.max_concurrent = max_concurrent
        self.try_variants = try_variants
        self.downloaded_urls: Set[str] = set()
        self.stats = {
            "llms_txt_files": 0,
            "doc_pages": 0,
            "errors": 0,
            "skipped": 0,
        }
        self.session: Optional[aiohttp.ClientSession] = None
        self.semaphore: Optional[asyncio.Semaphore] = None

    async def __aenter__(self):
        """Async context manager entry."""
        self.session = aiohttp.ClientSession(
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; LLMDocsBot/1.0; +https://github.com)"
            },
            timeout=aiohttp.ClientTimeout(total=30),
        )
        self.semaphore = asyncio.Semaphore(self.max_concurrent)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.close()

    def is_valid_url(self, url: str) -> bool:
        """Validate URL before attempting to download."""
        if not url:
            return False

        # Filter out invalid schemes
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False

        # Filter out URLs with invalid characters
        invalid_chars = [")", "(", "|", "\\", "^", "`", "[", "]", "{", "}"]
        if any(char in url for char in invalid_chars):
            return False

        # Filter out common non-documentation patterns
        if url.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico")):
            return False

        return True

    def generate_url_variants(self, url: str) -> List[str]:
        """Generate URL variants to try (.md, .mdx extensions)."""
        variants = [url]

        # Don't add variants for URLs that already have extensions
        if url.endswith(('.md', '.mdx', '.html', '.txt', '.pdf')):
            return variants

        # For URLs ending with /, try index.md and index.mdx
        if url.endswith('/'):
            variants.extend([
                f"{url}index.md",
                f"{url}index.mdx",
            ])
        else:
            # Try adding .md and .mdx extensions
            variants.extend([
                f"{url}.md",
                f"{url}.mdx",
            ])

        return variants

    async def fetch_url(
        self, url: str, try_variants: bool = True
    ) -> Optional[str]:
        """Fetch URL content with retries and error handling."""
        if not self.is_valid_url(url):
            print(f"  Skipping invalid URL: {url}")
            self.stats["skipped"] += 1
            return None

        # Generate URL variants to try
        urls_to_try = self.generate_url_variants(url) if try_variants else [url]

        for url_variant in urls_to_try:
            for attempt in range(self.max_retries):
                try:
                    async with self.semaphore:
                        if url_variant != url:
                            print(f"  Trying variant: {url_variant}")
                        else:
                            print(f"  Fetching: {url_variant}")

                        async with self.session.get(url_variant) as response:
                            response.raise_for_status()
                            content = await response.text()

                            if url_variant != url:
                                print(f"  ✓ Success with variant: {url_variant}")

                            return content
                except aiohttp.ClientResponseError as e:
                    # Don't retry on 404/403 for variants, just try next variant
                    if e.status in (404, 403) and url_variant != url:
                        break  # Try next variant

                    if attempt < self.max_retries - 1:
                        wait_time = 2**attempt
                        print(
                            f"  Error ({e.status}): {url_variant}. "
                            f"Retrying in {wait_time}s..."
                        )
                        await asyncio.sleep(wait_time)
                    else:
                        if url_variant == urls_to_try[-1]:
                            print(f"  Failed all variants for {url}")
                            self.stats["errors"] += 1
                except (
                    aiohttp.ClientError,
                    asyncio.TimeoutError,
                    Exception,
                ) as e:
                    if attempt < self.max_retries - 1:
                        wait_time = 2**attempt
                        print(
                            f"  Error fetching {url_variant}: {e}. "
                            f"Retrying in {wait_time}s..."
                        )
                        await asyncio.sleep(wait_time)
                    else:
                        if url_variant == urls_to_try[-1]:
                            print(f"  Failed all variants for {url}: {e}")
                            self.stats["errors"] += 1

        return None

    def parse_llms_txt(self, content: str, base_url: str) -> Dict[str, any]:
        """
        Parse llms.txt file format.

        Expected format:
        # Project Name
        Description

        ## Section Name
        - https://example.com/doc1
        - https://example.com/doc2

        Or:
        https://example.com/doc1
        https://example.com/doc2
        """
        result = {"metadata": {}, "urls": []}

        lines = content.split("\n")
        current_section = None

        for line in lines:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Extract title from main header
            if line.startswith("#") and not line.startswith("##"):
                if not current_section:
                    result["metadata"]["title"] = line.lstrip("#").strip()
                continue

            # Section headers
            if line.startswith("##"):
                current_section = line.lstrip("#").strip()
                continue

            # Extract URLs - Handle markdown links: [title](url)
            md_links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", line)
            for title, url in md_links:
                # Clean up URL
                url = url.strip()
                full_url = urljoin(base_url, url)
                if self.is_valid_url(full_url):
                    result["urls"].append(full_url)

            # Handle plain URLs
            url_pattern = r"https?://[^\s<>\"{}|\\^`\[\])]+"
            urls = re.findall(url_pattern, line)
            for url in urls:
                # Skip if already captured as markdown link
                if not any(url in link[1] for link in md_links):
                    full_url = urljoin(base_url, url)
                    if self.is_valid_url(full_url):
                        result["urls"].append(full_url)

            # Handle relative paths (starting with /)
            if line.startswith("/") and not line.startswith("//"):
                full_url = urljoin(base_url, line)
                if self.is_valid_url(full_url):
                    result["urls"].append(full_url)

        return result

    def sanitize_filename(self, url: str) -> str:
        """Convert URL to safe filename."""
        parsed = urlparse(url)
        # Use domain and path
        domain = parsed.netloc.replace(":", "_")
        path = parsed.path.strip("/").replace("/", "_")

        # Handle index pages
        if not path or path == "index":
            path = "index"

        # Handle query parameters
        if parsed.query:
            # Keep first 50 chars of query
            query_part = re.sub(r"[^\w\-_.]", "_", parsed.query[:50])
            path = f"{path}_{query_part}"

        # Create filename
        filename = f"{domain}_{path}" if path else domain

        # Clean up
        filename = re.sub(r"[^\w\-_.]", "_", filename)
        filename = re.sub(r"_+", "_", filename)

        return filename[:200]  # Limit length

    def extract_main_content(self, html: str, url: str) -> str:
        """Extract main content from HTML page."""
        try:
            soup = BeautifulSoup(html, "lxml")
        except Exception:
            # Fallback to html.parser if lxml fails
            soup = BeautifulSoup(html, "html.parser")

        # Remove script and style elements
        for element in soup(
            ["script", "style", "nav", "header", "footer", "aside"]
        ):
            element.decompose()

        # Try to find main content area
        main_content = None
        for selector in [
            "main",
            "article",
            '[role="main"]',
            ".content",
            ".documentation",
            "#content",
        ]:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.find("body") or soup

        # Convert to markdown-ish format
        text = []
        text.append(
            f"# {soup.title.string if soup.title else 'Documentation'}\n"
        )
        text.append(f"Source: {url}\n")
        text.append(f"Downloaded: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        text.append("=" * 80 + "\n\n")

        # Get text content with some structure preserved
        for elem in main_content.find_all(
            ["h1", "h2", "h3", "h4", "h5", "h6", "p", "pre", "code", "li", "a"]
        ):
            if elem.name.startswith("h"):
                level = int(elem.name[1])
                text.append(f"\n{'#' * level} {elem.get_text(strip=True)}\n")
            elif elem.name == "pre":
                text.append(f"\n```\n{elem.get_text()}\n```\n")
            elif elem.name == "code" and elem.parent.name != "pre":
                text.append(f"`{elem.get_text(strip=True)}`")
            elif elem.name == "li":
                text.append(f"- {elem.get_text(strip=True)}\n")
            elif elem.name == "a":
                href = elem.get("href", "")
                if href:
                    full_href = urljoin(url, href)
                    text.append(
                        f"[{elem.get_text(strip=True)}]({full_href})"
                    )
            elif elem.name == "p":
                paragraph_text = elem.get_text(strip=True)
                if paragraph_text:
                    text.append(f"\n{paragraph_text}\n")

        return "".join(text)

    async def save_content(
        self, url: str, content: str, subdirectory: str = ""
    ) -> Path:
        """Save content to file asynchronously."""
        parsed = urlparse(url)
        domain = parsed.netloc

        # Create subdirectory for domain
        save_dir = (
            self.output_dir / subdirectory / domain
            if subdirectory
            else self.output_dir / domain
        )
        save_dir.mkdir(parents=True, exist_ok=True)

        # Generate filename
        filename = self.sanitize_filename(url)
        if not filename.endswith((".txt", ".md")):
            filename += ".md"

        filepath = save_dir / filename

        # Save file
        async with asyncio.Lock():
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

        print(f"  Saved: {filepath}")
        return filepath

    async def download_document(
        self, url: str, subdirectory: str = "docs", try_variants: bool = True
    ):
        """Download a single documentation page."""
        if url in self.downloaded_urls:
            print(f"\n  Skipping (already downloaded): {url}")
            self.stats["skipped"] += 1
            return

        self.downloaded_urls.add(url)

        print(f"\n  Downloading documentation: {url}")
        doc_content = await self.fetch_url(url, try_variants=try_variants)

        if doc_content:
            # Check if it's HTML or plain text
            if "<html" in doc_content.lower() or "<body" in doc_content.lower():
                doc_content = self.extract_main_content(doc_content, url)

            await self.save_content(url, doc_content, subdirectory=subdirectory)
            self.stats["doc_pages"] += 1

        # Rate limiting
        await asyncio.sleep(self.delay)

    async def download_llms_txt(self, url: str):
        """Download and process a single llms.txt file."""
        print(f"\n{'=' * 80}")
        print(f"Processing llms.txt: {url}")
        print(f"{'=' * 80}")

        content = await self.fetch_url(url)
        if not content:
            return

        self.stats["llms_txt_files"] += 1

        # Save the llms.txt file itself
        await self.save_content(url, content)

        # Parse and extract URLs
        parsed_data = self.parse_llms_txt(content, url)

        # Remove duplicates while preserving order
        unique_urls = list(dict.fromkeys(parsed_data["urls"]))

        print(f"\nFound {len(unique_urls)} documentation URLs")

        # Create metadata file
        parsed = urlparse(url)
        metadata_path = self.output_dir / parsed.netloc / "_metadata.json"
        async with asyncio.Lock():
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "source_url": url,
                        "downloaded_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "metadata": parsed_data["metadata"],
                        "doc_urls": unique_urls,
                    },
                    f,
                    indent=2,
                )

        # Download all referenced documentation in parallel
        tasks = [
            self.download_document(doc_url, try_variants=self.try_variants)
            for doc_url in unique_urls
        ]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def download_from_list(self, urls: List[str]):
        """Download documentation from a list of llms.txt URLs."""
        print(f"Starting download of {len(urls)} llms.txt files...")

        for url in urls:
            try:
                await self.download_llms_txt(url)
            except Exception as e:
                print(f"Error processing {url}: {e}")
                self.stats["errors"] += 1

        self.print_stats()

    def print_stats(self):
        """Print download statistics."""
        print(f"\n{'=' * 80}")
        print("Download Statistics:")
        print(f"{'=' * 80}")
        print(f"llms.txt files processed: {self.stats['llms_txt_files']}")
        print(f"Documentation pages downloaded: {self.stats['doc_pages']}")
        print(f"Pages skipped (duplicates/invalid): {self.stats['skipped']}")
        print(f"Errors encountered: {self.stats['errors']}")
        print(f"\nOutput directory: {self.output_dir.absolute()}")
        print(f"{'=' * 80}\n")


async def async_main(
    urls: List[str],
    output_dir: str,
    delay: float,
    max_retries: int,
    max_concurrent: int,
    try_variants: bool,
):
    """Async main function."""
    async with LLMDocsDownloader(
        output_dir=output_dir,
        delay=delay,
        max_retries=max_retries,
        max_concurrent=max_concurrent,
        try_variants=try_variants,
    ) as downloader:
        await downloader.download_from_list(urls)


def main():
    parser = argparse.ArgumentParser(
        description="Download LLM documentation from llms.txt files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://docs.cursor.com/llms-full.txt https://docs.claude.com/llms.txt
  %(prog)s --config urls.txt --output my_docs
  %(prog)s --url https://linear.app/llms.txt --delay 0.1 --concurrent 20
        """,
    )

    parser.add_argument("urls", nargs="*", help="llms.txt URLs to download")
    parser.add_argument(
        "--config",
        "-c",
        help="File containing list of URLs (one per line)",
    )
    parser.add_argument(
        "--url",
        "-u",
        action="append",
        help="Single URL to download (can be used multiple times)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="llm_docs",
        help="Output directory (default: llm_docs)",
    )
    parser.add_argument(
        "--delay",
        "-d",
        type=float,
        default=0.1,
        help="Delay between requests in seconds (default: 0.1)",
    )
    parser.add_argument(
        "--max-retries",
        "-r",
        type=int,
        default=3,
        help="Maximum retries for failed requests (default: 3)",
    )
    parser.add_argument(
        "--concurrent",
        "-j",
        type=int,
        default=10,
        help="Maximum concurrent downloads (default: 10)",
    )
    parser.add_argument(
        "--try-variants",
        action="store_true",
        default=True,
        help="Try .md and .mdx variants for URLs (default: enabled)",
    )
    parser.add_argument(
        "--no-variants",
        action="store_false",
        dest="try_variants",
        help="Disable trying .md and .mdx variants",
    )

    args = parser.parse_args()

    # Collect all URLs from different sources
    all_urls = []

    # From positional arguments
    if args.urls:
        all_urls.extend(args.urls)

    # From --url flags
    if args.url:
        all_urls.extend(args.url)

    # From config file
    if args.config:
        try:
            with open(args.config, "r") as f:
                file_urls = [
                    line.strip()
                    for line in f
                    if line.strip() and not line.startswith("#")
                ]
                all_urls.extend(file_urls)
        except FileNotFoundError:
            print(f"Error: Config file '{args.config}' not found")
            sys.exit(1)

    # If no URLs provided, show help
    if not all_urls:
        print("No URLs provided. Use --help for usage information.")
        print("\nExample URLs:")
        print("  https://docs.cursor.com/llms-full.txt")
        print("  https://docs.claude.com/llms.txt")
        print("  https://linear.app/llms.txt")
        print("  https://railway.com/llms.txt")
        print("  https://docs.mem0.ai/llms.txt")
        sys.exit(1)

    # Remove duplicates while preserving order
    all_urls = list(dict.fromkeys(all_urls))

    # Run async main
    asyncio.run(
        async_main(
            urls=all_urls,
            output_dir=args.output,
            delay=args.delay,
            max_retries=args.max_retries,
            max_concurrent=args.concurrent,
            try_variants=args.try_variants,
        )
    )


if __name__ == "__main__":
    main()
