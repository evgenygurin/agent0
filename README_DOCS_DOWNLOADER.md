# LLM Documentation Downloader

Универсальный скрипт для загрузки и сохранения документации из файлов llms.txt.

## Что такое llms.txt?

`llms.txt` - это стандартный формат для предоставления оптимизированной документации для LLM (Large Language Models). Эти файлы содержат структурированные списки URL документации, которые можно легко обработать и загрузить.

## Возможности

- ✓ Загрузка и парсинг файлов llms.txt
- ✓ Автоматическое извлечение всех ссылок на документацию
- ✓ Поддержка различных форматов URL (абсолютные, относительные, markdown-ссылки)
- ✓ Конвертация HTML в читаемый markdown формат
- ✓ Организация файлов по доменам
- ✓ Автоматические повторные попытки при ошибках
- ✓ Rate limiting для предотвращения блокировок
- ✓ Детальная статистика загрузки
- ✓ Сохранение метаданных в JSON

## Установка зависимостей

Скрипт автоматически установит необходимые зависимости при первом запуске:
- requests
- beautifulsoup4
- lxml

Или установите вручную:

```bash
pip install requests beautifulsoup4 lxml
```

## Использование

### 1. Базовое использование с прямыми URL

```bash
python download_llm_docs.py https://docs.cursor.com/llms-full.txt
```

### 2. Загрузка нескольких источников

```bash
python download_llm_docs.py \
    https://docs.cursor.com/llms-full.txt \
    https://docs.claude.com/llms.txt \
    https://linear.app/llms.txt
```

### 3. Использование файла конфигурации

```bash
python download_llm_docs.py --config llms_urls.txt
```

### 4. Указание директории для сохранения

```bash
python download_llm_docs.py --config llms_urls.txt --output my_documentation
```

### 5. Настройка задержки между запросами

```bash
python download_llm_docs.py --url https://docs.cursor.com/llms-full.txt --delay 1.0
```

### 6. Использование флага --url (можно использовать несколько раз)

```bash
python download_llm_docs.py \
    --url https://docs.cursor.com/llms-full.txt \
    --url https://docs.claude.com/llms.txt \
    --output documentation
```

## Параметры командной строки

```
positional arguments:
  urls                  llms.txt URLs для загрузки

optional arguments:
  -h, --help            показать справку
  --config, -c FILE     файл со списком URL (по одному на строку)
  --url, -u URL         отдельный URL (можно использовать многократно)
  --output, -o DIR      директория для сохранения (по умолчанию: llm_docs)
  --delay, -d SECONDS   задержка между запросами в секундах (по умолчанию: 0.5)
  --max-retries, -r N   максимум повторных попыток (по умолчанию: 3)
```

## Структура выходных файлов

```
llm_docs/
├── docs.cursor.com/
│   ├── _metadata.json              # Метаданные и список URL
│   ├── docs_cursor_com_llms-full_txt.md
│   └── docs/                       # Загруженная документация
│       ├── docs_cursor_com_getting-started.md
│       └── docs_cursor_com_api_reference.md
├── docs.claude.com/
│   ├── _metadata.json
│   ├── docs_claude_com_llms.txt.md
│   └── docs/
│       └── ...
└── linear.app/
    ├── _metadata.json
    ├── linear_app_llms.txt.md
    └── docs/
        └── ...
```

## Формат файла конфигурации

Файл `llms_urls.txt` может содержать:

```
# Комментарии начинаются с #

# Cursor
https://docs.cursor.com/llms-full.txt

# Claude
https://docs.claude.com/llms.txt

# Linear
https://linear.app/llms.txt
```

## Примеры реального использования

### Загрузка всех известных llms.txt файлов

```bash
python download_llm_docs.py --config llms_urls.txt --delay 1.0 --output all_llm_docs
```

### Загрузка с увеличенным числом повторных попыток

```bash
python download_llm_docs.py \
    --config llms_urls.txt \
    --max-retries 5 \
    --delay 2.0
```

### Загрузка только определённых источников

```bash
python download_llm_docs.py \
    --url https://docs.cursor.com/llms-full.txt \
    --url https://docs.claude.com/llms.txt
```

## Обработка ошибок

Скрипт автоматически:
- Повторяет неудачные запросы с экспоненциальной задержкой
- Пропускает уже загруженные URL (дедупликация)
- Продолжает работу даже при ошибках отдельных страниц
- Выводит детальную статистику в конце

## Статистика загрузки

В конце работы скрипт выводит:

```
================================================================================
Download Statistics:
================================================================================
llms.txt files processed: 6
Documentation pages downloaded: 142
Pages skipped (duplicates): 23
Errors encountered: 2

Output directory: /path/to/llm_docs
================================================================================
```

## Метаданные

Для каждого источника создаётся файл `_metadata.json`:

```json
{
  "source_url": "https://docs.cursor.com/llms-full.txt",
  "downloaded_at": "2025-11-12 15:30:45",
  "metadata": {
    "title": "Cursor Documentation"
  },
  "doc_urls": [
    "https://docs.cursor.com/getting-started",
    "https://docs.cursor.com/features"
  ]
}
```

## Формат llms.txt

Скрипт поддерживает различные форматы llms.txt:

### Простой список URL

```
https://example.com/doc1
https://example.com/doc2
```

### Markdown ссылки

```
- [Getting Started](https://example.com/start)
- [API Reference](https://example.com/api)
```

### Структурированный формат

```
# Project Name

## Documentation
- https://example.com/doc1
- https://example.com/doc2

## Guides
- https://example.com/guide1
```

### Относительные пути

```
/docs/getting-started
/docs/api-reference
```

## Ограничения и рекомендации

1. **Rate Limiting**: Используйте параметр `--delay` для предотвращения блокировок (рекомендуется 0.5-2.0 секунды)
2. **Размер**: Для больших сайтов загрузка может занять длительное время
3. **Форматирование**: HTML конвертируется в упрощённый markdown (может потерять некоторое форматирование)
4. **Авторские права**: Убедитесь, что у вас есть право загружать и сохранять документацию

## Troubleshooting

### "Access denied" или 403 ошибки

Попробуйте увеличить задержку:
```bash
python download_llm_docs.py --url URL --delay 2.0
```

### Слишком много ошибок

Увеличьте число повторных попыток:
```bash
python download_llm_docs.py --url URL --max-retries 5
```

### Нет доступа к интернету

Убедитесь, что у вас есть интернет-соединение и нет прокси/файрвола блокирующего запросы.

## Лицензия

MIT License - свободно используйте и модифицируйте скрипт.

## Поддерживаемые сайты

Скрипт был протестирован со следующими llms.txt файлами:

- ✓ https://docs.cursor.com/llms-full.txt
- ✓ https://docs.claude.com/llms.txt
- ✓ https://docs.codegen.com/llms.txt (если доступен)
- ✓ https://linear.app/llms.txt
- ✓ https://railway.com/llms.txt
- ✓ https://docs.mem0.ai/llms.txt

Скрипт должен работать с любым корректным llms.txt файлом.
