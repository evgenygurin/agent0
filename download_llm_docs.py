#!/usr/bin/env python3
"""
Universal LLM Documentation Downloader

This script downloads and saves documentation from llms.txt files.
llms.txt is a standard format for providing LLM-optimized documentation.

Usage:
    python download_llm_docs.py [URLs...]
    python download_llm_docs.py --config urls.txt
    python download_llm_docs.py --url https://docs.example.com/llms.txt
"""

import argparse
import os
import sys
import time
import json
from pathlib import Path
from typing import List, Dict, Set, Optional
from urllib.parse import urljoin, urlparse
import re

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing required dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "requests", "beautifulsoup4", "lxml"])
    import requests
    from bs4 import BeautifulSoup


class LLMDocsDownloader:
    """Downloads and organizes LLM documentation from llms.txt files."""

    def __init__(self, output_dir: str = "llm_docs", delay: float = 0.5, max_retries: int = 3):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.delay = delay
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; LLMDocsBot/1.0; +https://github.com)'
        })
        self.downloaded_urls: Set[str] = set()
        self.stats = {
            'llms_txt_files': 0,
            'doc_pages': 0,
            'errors': 0,
            'skipped': 0
        }

    def fetch_url(self, url: str) -> Optional[str]:
        """Fetch URL content with retries and error handling."""
        for attempt in range(self.max_retries):
            try:
                print(f"  Fetching: {url}")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                return response.text
            except requests.exceptions.RequestException as e:
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"  Error fetching {url}: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"  Failed to fetch {url}: {e}")
                    self.stats['errors'] += 1
                    return None
        return None

    def parse_llms_txt(self, content: str, base_url: str) -> Dict[str, List[str]]:
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
        result = {
            'metadata': {},
            'urls': []
        }

        lines = content.split('\n')
        current_section = None

        for line in lines:
            line = line.strip()

            # Skip empty lines and comments (unless they're markdown headers)
            if not line or (line.startswith('#') and not line.startswith('##')):
                if line.startswith('#') and not current_section:
                    result['metadata']['title'] = line.lstrip('#').strip()
                continue

            # Section headers
            if line.startswith('##'):
                current_section = line.lstrip('#').strip()
                continue

            # Extract URLs
            # Handle markdown links: [title](url)
            md_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', line)
            for title, url in md_links:
                full_url = urljoin(base_url, url)
                result['urls'].append(full_url)

            # Handle plain URLs
            url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
            urls = re.findall(url_pattern, line)
            for url in urls:
                # Skip if already captured as markdown link
                if not any(url in link[1] for link in md_links):
                    full_url = urljoin(base_url, url)
                    result['urls'].append(full_url)

            # Handle relative paths (starting with /)
            if line.startswith('/'):
                full_url = urljoin(base_url, line)
                result['urls'].append(full_url)

        return result

    def sanitize_filename(self, url: str) -> str:
        """Convert URL to safe filename."""
        parsed = urlparse(url)
        # Use domain and path
        domain = parsed.netloc.replace(':', '_')
        path = parsed.path.strip('/').replace('/', '_')

        # Handle index pages
        if not path or path == 'index':
            path = 'index'

        # Remove query parameters but keep meaningful ones
        filename = f"{domain}_{path}" if path else domain

        # Clean up
        filename = re.sub(r'[^\w\-_.]', '_', filename)
        filename = re.sub(r'_+', '_', filename)

        return filename[:200]  # Limit length

    def extract_main_content(self, html: str, url: str) -> str:
        """Extract main content from HTML page."""
        soup = BeautifulSoup(html, 'lxml')

        # Remove script and style elements
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            element.decompose()

        # Try to find main content area
        main_content = None
        for selector in ['main', 'article', '[role="main"]', '.content', '.documentation', '#content']:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.find('body') or soup

        # Convert to markdown-ish format
        text = []
        text.append(f"# {soup.title.string if soup.title else 'Documentation'}\n")
        text.append(f"Source: {url}\n")
        text.append(f"Downloaded: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        text.append("=" * 80 + "\n\n")

        # Get text content with some structure preserved
        for elem in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'code', 'li', 'a']):
            if elem.name.startswith('h'):
                level = int(elem.name[1])
                text.append(f"\n{'#' * level} {elem.get_text(strip=True)}\n")
            elif elem.name == 'pre':
                text.append(f"\n```\n{elem.get_text()}\n```\n")
            elif elem.name == 'code' and elem.parent.name != 'pre':
                text.append(f"`{elem.get_text(strip=True)}`")
            elif elem.name == 'li':
                text.append(f"- {elem.get_text(strip=True)}\n")
            elif elem.name == 'a':
                href = elem.get('href', '')
                if href:
                    full_href = urljoin(url, href)
                    text.append(f"[{elem.get_text(strip=True)}]({full_href})")
            elif elem.name == 'p':
                paragraph_text = elem.get_text(strip=True)
                if paragraph_text:
                    text.append(f"\n{paragraph_text}\n")

        return ''.join(text)

    def save_content(self, url: str, content: str, subdirectory: str = ""):
        """Save content to file."""
        parsed = urlparse(url)
        domain = parsed.netloc

        # Create subdirectory for domain
        save_dir = self.output_dir / subdirectory / domain if subdirectory else self.output_dir / domain
        save_dir.mkdir(parents=True, exist_ok=True)

        # Generate filename
        filename = self.sanitize_filename(url)
        if not filename.endswith(('.txt', '.md')):
            filename += '.md'

        filepath = save_dir / filename

        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Saved: {filepath}")
        return filepath

    def download_llms_txt(self, url: str):
        """Download and process a single llms.txt file."""
        print(f"\n{'=' * 80}")
        print(f"Processing llms.txt: {url}")
        print(f"{'=' * 80}")

        content = self.fetch_url(url)
        if not content:
            return

        self.stats['llms_txt_files'] += 1

        # Save the llms.txt file itself
        self.save_content(url, content)

        # Parse and extract URLs
        parsed_data = self.parse_llms_txt(content, url)

        print(f"\nFound {len(parsed_data['urls'])} documentation URLs")

        # Create metadata file
        metadata_path = self.output_dir / urlparse(url).netloc / '_metadata.json'
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump({
                'source_url': url,
                'downloaded_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                'metadata': parsed_data['metadata'],
                'doc_urls': parsed_data['urls']
            }, f, indent=2)

        # Download all referenced documentation
        for doc_url in parsed_data['urls']:
            if doc_url in self.downloaded_urls:
                print(f"\n  Skipping (already downloaded): {doc_url}")
                self.stats['skipped'] += 1
                continue

            self.downloaded_urls.add(doc_url)

            print(f"\n  Downloading documentation: {doc_url}")
            doc_content = self.fetch_url(doc_url)

            if doc_content:
                # Check if it's HTML or plain text
                if '<html' in doc_content.lower() or '<body' in doc_content.lower():
                    doc_content = self.extract_main_content(doc_content, doc_url)

                self.save_content(doc_url, doc_content, subdirectory="docs")
                self.stats['doc_pages'] += 1

            # Rate limiting
            time.sleep(self.delay)

    def download_from_list(self, urls: List[str]):
        """Download documentation from a list of llms.txt URLs."""
        print(f"Starting download of {len(urls)} llms.txt files...")

        for url in urls:
            try:
                self.download_llms_txt(url)
            except Exception as e:
                print(f"Error processing {url}: {e}")
                self.stats['errors'] += 1

        self.print_stats()

    def print_stats(self):
        """Print download statistics."""
        print(f"\n{'=' * 80}")
        print("Download Statistics:")
        print(f"{'=' * 80}")
        print(f"llms.txt files processed: {self.stats['llms_txt_files']}")
        print(f"Documentation pages downloaded: {self.stats['doc_pages']}")
        print(f"Pages skipped (duplicates): {self.stats['skipped']}")
        print(f"Errors encountered: {self.stats['errors']}")
        print(f"\nOutput directory: {self.output_dir.absolute()}")
        print(f"{'=' * 80}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Download LLM documentation from llms.txt files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://docs.cursor.com/llms-full.txt https://docs.claude.com/llms.txt
  %(prog)s --config urls.txt --output my_docs
  %(prog)s --url https://linear.app/llms.txt --delay 1.0
        """
    )

    parser.add_argument('urls', nargs='*', help='llms.txt URLs to download')
    parser.add_argument('--config', '-c', help='File containing list of URLs (one per line)')
    parser.add_argument('--url', '-u', action='append', help='Single URL to download (can be used multiple times)')
    parser.add_argument('--output', '-o', default='llm_docs', help='Output directory (default: llm_docs)')
    parser.add_argument('--delay', '-d', type=float, default=0.5, help='Delay between requests in seconds (default: 0.5)')
    parser.add_argument('--max-retries', '-r', type=int, default=3, help='Maximum retries for failed requests (default: 3)')

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
            with open(args.config, 'r') as f:
                file_urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                all_urls.extend(file_urls)
        except FileNotFoundError:
            print(f"Error: Config file '{args.config}' not found")
            sys.exit(1)

    # If no URLs provided, use default list
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

    # Create downloader and start downloading
    downloader = LLMDocsDownloader(
        output_dir=args.output,
        delay=args.delay,
        max_retries=args.max_retries
    )

    downloader.download_from_list(all_urls)


if __name__ == '__main__':
    main()
