#!/usr/bin/env python3
"""
Демонстрация работы парсера llms.txt с примерами данных
"""

from download_llm_docs import LLMDocsDownloader
import tempfile
import os

def create_sample_llms_txt():
    """Создать пример llms.txt файла"""
    return """# Cursor Documentation

Cursor is an AI-powered code editor.

## Getting Started
- https://docs.cursor.com/getting-started
- https://docs.cursor.com/installation

## Features
- [AI Chat](https://docs.cursor.com/features/chat)
- [Code Generation](https://docs.cursor.com/features/codegen)
- [Tab Completion](https://docs.cursor.com/features/tab)

## API Reference
https://docs.cursor.com/api/overview
https://docs.cursor.com/api/settings

## Advanced
/docs/advanced/shortcuts
/docs/advanced/customization
"""

def create_sample_html_doc():
    """Создать пример HTML документации"""
    return """<!DOCTYPE html>
<html>
<head>
    <title>Getting Started with Cursor</title>
</head>
<body>
    <header>
        <nav>Navigation menu</nav>
    </header>

    <main>
        <h1>Getting Started</h1>

        <p>Welcome to Cursor, the AI-powered code editor!</p>

        <h2>Installation</h2>

        <p>To install Cursor, follow these steps:</p>

        <ol>
            <li>Download from the official website</li>
            <li>Run the installer</li>
            <li>Open Cursor</li>
        </ol>

        <h2>First Steps</h2>

        <p>Try these features:</p>

        <ul>
            <li>AI Chat - Ask questions about your code</li>
            <li>Code Generation - Generate code with AI</li>
            <li>Tab Completion - Smart autocomplete</li>
        </ul>

        <h3>Example Code</h3>

        <pre><code>
def hello_world():
    print("Hello from Cursor!")
        </code></pre>

        <p>Learn more in our <a href="/docs/advanced">advanced documentation</a>.</p>
    </main>

    <footer>
        <p>Copyright 2024</p>
    </footer>
</body>
</html>
"""

def demo_parse_llms_txt():
    """Демонстрация парсинга llms.txt"""
    print("=" * 80)
    print("ДЕМО 1: Парсинг llms.txt файла")
    print("=" * 80)

    downloader = LLMDocsDownloader(output_dir="demo_output")

    sample_content = create_sample_llms_txt()
    print("\nИсходный llms.txt файл:")
    print("-" * 80)
    print(sample_content)
    print("-" * 80)

    parsed = downloader.parse_llms_txt(sample_content, "https://docs.cursor.com/llms.txt")

    print(f"\n📊 Результаты парсинга:")
    print(f"  Название проекта: {parsed['metadata'].get('title', 'N/A')}")
    print(f"  Найдено URL: {len(parsed['urls'])}")
    print(f"\n📝 Извлечённые URL:")
    for i, url in enumerate(parsed['urls'], 1):
        print(f"  {i}. {url}")

    return parsed

def demo_extract_html_content():
    """Демонстрация извлечения контента из HTML"""
    print("\n\n" + "=" * 80)
    print("ДЕМО 2: Извлечение контента из HTML")
    print("=" * 80)

    downloader = LLMDocsDownloader(output_dir="demo_output")

    sample_html = create_sample_html_doc()
    print("\nИсходный HTML (первые 500 символов):")
    print("-" * 80)
    print(sample_html[:500] + "...")
    print("-" * 80)

    extracted = downloader.extract_main_content(
        sample_html,
        "https://docs.cursor.com/getting-started"
    )

    print("\n📄 Извлечённый контент (markdown):")
    print("-" * 80)
    print(extracted[:800] + "\n..." if len(extracted) > 800 else extracted)
    print("-" * 80)

    return extracted

def demo_filename_sanitization():
    """Демонстрация создания безопасных имён файлов"""
    print("\n\n" + "=" * 80)
    print("ДЕМО 3: Генерация безопасных имён файлов")
    print("=" * 80)

    downloader = LLMDocsDownloader(output_dir="demo_output")

    test_urls = [
        "https://docs.cursor.com/getting-started",
        "https://docs.cursor.com/api/v1/settings",
        "https://example.com/docs/advanced/shortcuts?version=2",
        "https://api.example.com:8080/docs/index",
        "https://docs.example.com/guide/installation#step-1",
    ]

    print("\n🔧 URL → Имя файла:")
    for url in test_urls:
        filename = downloader.sanitize_filename(url)
        print(f"  {url}")
        print(f"  → {filename}.md\n")

def demo_supported_formats():
    """Демонстрация поддерживаемых форматов llms.txt"""
    print("\n\n" + "=" * 80)
    print("ДЕМО 4: Поддерживаемые форматы llms.txt")
    print("=" * 80)

    downloader = LLMDocsDownloader(output_dir="demo_output")

    formats = {
        "Простой список URL": """
https://example.com/doc1
https://example.com/doc2
https://example.com/doc3
""",
        "Markdown ссылки": """
- [Getting Started](https://example.com/start)
- [API Reference](https://example.com/api)
- [Examples](https://example.com/examples)
""",
        "Структурированный формат": """
# Project Documentation

## Guides
- https://example.com/guide1
- https://example.com/guide2

## API
- https://example.com/api/v1
""",
        "Относительные пути": """
/docs/getting-started
/docs/api-reference
/docs/examples
"""
    }

    for format_name, content in formats.items():
        print(f"\n📋 {format_name}:")
        print("-" * 40)
        print(content.strip())

        parsed = downloader.parse_llms_txt(content, "https://example.com/llms.txt")
        print(f"\n  ✓ Извлечено URL: {len(parsed['urls'])}")
        for url in parsed['urls']:
            print(f"    • {url}")

def demo_statistics():
    """Демонстрация статистики"""
    print("\n\n" + "=" * 80)
    print("ДЕМО 5: Структура статистики")
    print("=" * 80)

    downloader = LLMDocsDownloader(output_dir="demo_output")

    # Симулируем некоторую активность
    downloader.stats['llms_txt_files'] = 3
    downloader.stats['doc_pages'] = 45
    downloader.stats['errors'] = 2
    downloader.stats['skipped'] = 8

    print("\n📈 Пример статистики после загрузки:")
    downloader.print_stats()

def main():
    print("\n🚀 ДЕМОНСТРАЦИЯ ВОЗМОЖНОСТЕЙ LLM DOCS DOWNLOADER")
    print("=" * 80)
    print("Этот демо показывает работу парсера llms.txt без доступа к интернету")
    print("=" * 80)

    # Запускаем все демо
    demo_parse_llms_txt()
    demo_extract_html_content()
    demo_filename_sanitization()
    demo_supported_formats()
    demo_statistics()

    print("\n\n" + "=" * 80)
    print("✅ ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 80)
    print("\nСкрипт успешно обрабатывает:")
    print("  ✓ Парсинг различных форматов llms.txt")
    print("  ✓ Извлечение URL из разных форматов")
    print("  ✓ Конвертация HTML в Markdown")
    print("  ✓ Генерация безопасных имён файлов")
    print("  ✓ Сбор статистики загрузки")
    print("\n💡 В реальной среде с доступом к интернету скрипт загрузит")
    print("   всю документацию с указанных сайтов автоматически.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
