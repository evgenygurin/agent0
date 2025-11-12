# Quick Start Guide

## Быстрый старт за 3 шага

### 1. Установите зависимости

```bash
pip install requests beautifulsoup4 lxml
```

Или просто запустите скрипт - зависимости установятся автоматически.

### 2. Загрузите документацию

Вариант A: Используйте готовый файл конфигурации

```bash
python download_llm_docs.py --config llms_urls.txt
```

Вариант B: Укажите URL напрямую

```bash
python download_llm_docs.py https://docs.cursor.com/llms-full.txt
```

Вариант C: Загрузите несколько источников

```bash
python download_llm_docs.py \
    https://docs.cursor.com/llms-full.txt \
    https://docs.claude.com/llms.txt \
    https://linear.app/llms.txt
```

### 3. Найдите результаты

Документация будет сохранена в директории `llm_docs/`:

```bash
ls -la llm_docs/
```

## Примеры команд

### Базовая загрузка с задержкой 1 секунда

```bash
python download_llm_docs.py --config llms_urls.txt --delay 1.0
```

### Загрузка в кастомную директорию

```bash
python download_llm_docs.py --config llms_urls.txt --output my_docs
```

### Загрузка с увеличенным числом повторных попыток

```bash
python download_llm_docs.py \
    --config llms_urls.txt \
    --max-retries 5 \
    --delay 2.0
```

## Программное использование

```python
from download_llm_docs import LLMDocsDownloader

downloader = LLMDocsDownloader(output_dir="docs")
downloader.download_llms_txt("https://docs.cursor.com/llms-full.txt")
```

Или запустите примеры:

```bash
python example_usage.py 1  # Базовый пример
python example_usage.py 5  # Загрузка из файла конфигурации
```

## Что дальше?

- Прочитайте [полную документацию](README_DOCS_DOWNLOADER.md)
- Настройте свой [список URL](llms_urls.txt)
- Изучите [примеры использования](example_usage.py)

## Помощь

Справка по всем параметрам:

```bash
python download_llm_docs.py --help
```
