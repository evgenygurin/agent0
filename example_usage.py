#!/usr/bin/env python3
"""
Пример программного использования LLMDocsDownloader
"""

from download_llm_docs import LLMDocsDownloader

# Пример 1: Базовое использование
def example_basic():
    """Базовый пример загрузки одного источника"""
    downloader = LLMDocsDownloader(output_dir="example_docs")

    urls = [
        "https://docs.cursor.com/llms-full.txt"
    ]

    downloader.download_from_list(urls)


# Пример 2: Настройка параметров
def example_custom_settings():
    """Пример с кастомными настройками"""
    downloader = LLMDocsDownloader(
        output_dir="custom_docs",
        delay=1.0,  # Увеличенная задержка
        max_retries=5  # Больше повторных попыток
    )

    urls = [
        "https://docs.claude.com/llms.txt",
        "https://linear.app/llms.txt"
    ]

    downloader.download_from_list(urls)


# Пример 3: Загрузка с обработкой результатов
def example_with_stats():
    """Пример с анализом статистики"""
    downloader = LLMDocsDownloader(output_dir="stats_docs")

    urls = [
        "https://docs.cursor.com/llms-full.txt",
        "https://docs.claude.com/llms.txt",
        "https://linear.app/llms.txt",
        "https://railway.com/llms.txt",
        "https://docs.mem0.ai/llms.txt"
    ]

    downloader.download_from_list(urls)

    # Вывод дополнительной информации
    print("\nДетальная статистика:")
    print(f"Всего уникальных URL: {len(downloader.downloaded_urls)}")
    print(f"Успешность: {(downloader.stats['doc_pages'] / max(len(downloader.downloaded_urls), 1)) * 100:.1f}%")


# Пример 4: Загрузка одного llms.txt файла
def example_single_file():
    """Пример загрузки одного файла"""
    downloader = LLMDocsDownloader(output_dir="single_doc")

    # Загрузка конкретного источника
    downloader.download_llms_txt("https://docs.cursor.com/llms-full.txt")

    downloader.print_stats()


# Пример 5: Чтение URL из файла
def example_from_file():
    """Пример чтения URL из файла конфигурации"""
    downloader = LLMDocsDownloader(output_dir="file_based_docs")

    # Читаем URL из файла
    urls = []
    try:
        with open("llms_urls.txt", "r") as f:
            for line in f:
                line = line.strip()
                # Пропускаем комментарии и пустые строки
                if line and not line.startswith('#'):
                    urls.append(line)
    except FileNotFoundError:
        print("Файл llms_urls.txt не найден")
        return

    print(f"Загружено {len(urls)} URL из файла конфигурации")
    downloader.download_from_list(urls)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        examples = {
            '1': example_basic,
            '2': example_custom_settings,
            '3': example_with_stats,
            '4': example_single_file,
            '5': example_from_file
        }

        if example_num in examples:
            print(f"Запуск примера {example_num}...")
            examples[example_num]()
        else:
            print(f"Неизвестный пример: {example_num}")
            print(f"Доступные примеры: {', '.join(examples.keys())}")
    else:
        print("Использование: python example_usage.py [1-5]")
        print("\nДоступные примеры:")
        print("  1 - Базовое использование")
        print("  2 - Настройка параметров")
        print("  3 - Загрузка с анализом статистики")
        print("  4 - Загрузка одного файла")
        print("  5 - Чтение URL из файла конфигурации")
