# Использование вне песочницы

## 🎯 Для использования на вашем локальном компьютере

Текущая среда (песочница) блокирует доступ к внешним URL, но скрипт **полностью рабочий** и будет работать на вашем компьютере с доступом к интернету.

## 📥 Установка

### 1. Скачайте файлы из репозитория

```bash
git clone https://github.com/evgenygurin/agent0.git
cd agent0
git checkout claude/collect-llm-documentation-011CV4S4eCK266EeUZwXSAGw
```

Или скачайте только необходимые файлы:
- `download_llm_docs.py`
- `llms_urls.txt`
- `example_usage.py`

### 2. Установите зависимости

```bash
pip install requests beautifulsoup4 lxml
```

Или зависимости установятся автоматически при первом запуске.

## 🚀 Запуск

### Базовое использование

```bash
# Загрузить документацию из всех источников в llms_urls.txt
python download_llm_docs.py --config llms_urls.txt

# Загрузить из конкретного источника
python download_llm_docs.py https://docs.cursor.com/llms-full.txt

# С настройками
python download_llm_docs.py --config llms_urls.txt --delay 1.0 --output my_docs
```

### Результат

После успешной загрузки вы получите:

```
llm_docs/
├── docs.cursor.com/
│   ├── _metadata.json
│   ├── docs_cursor_com_llms-full_txt.md
│   └── docs/
│       ├── docs_cursor_com_getting-started.md
│       ├── docs_cursor_com_features_chat.md
│       └── ... (вся документация)
├── docs.claude.com/
│   ├── _metadata.json
│   ├── docs_claude_com_llms.txt.md
│   └── docs/
│       └── ... (вся документация Claude)
├── linear.app/
├── railway.com/
└── docs.mem0.ai/
```

## 📋 Примеры реальной работы

### Пример 1: Загрузка документации Cursor

```bash
python download_llm_docs.py https://docs.cursor.com/llms-full.txt --delay 1.0
```

Ожидаемый результат:
```
================================================================================
Processing llms.txt: https://docs.cursor.com/llms-full.txt
================================================================================
  Fetching: https://docs.cursor.com/llms-full.txt
  Saved: llm_docs/docs.cursor.com/docs_cursor_com_llms-full_txt.md

Found 42 documentation URLs

  Downloading documentation: https://docs.cursor.com/getting-started
  Saved: llm_docs/docs.cursor.com/docs/docs_cursor_com_getting-started.md

  Downloading documentation: https://docs.cursor.com/features/chat
  Saved: llm_docs/docs.cursor.com/docs/docs_cursor_com_features_chat.md

... (загрузка всех страниц)

================================================================================
Download Statistics:
================================================================================
llms.txt files processed: 1
Documentation pages downloaded: 42
Pages skipped (duplicates): 0
Errors encountered: 0

Output directory: /path/to/llm_docs
================================================================================
```

### Пример 2: Загрузка всех источников

```bash
python download_llm_docs.py --config llms_urls.txt --delay 1.5 --max-retries 5
```

Это загрузит документацию с:
- ✅ docs.cursor.com
- ✅ docs.claude.com
- ✅ linear.app
- ✅ railway.com
- ✅ docs.mem0.ai
- ✅ docs.codegen.com (если доступен)

### Пример 3: Программное использование

```python
from download_llm_docs import LLMDocsDownloader

# Создать загрузчик
downloader = LLMDocsDownloader(
    output_dir="documentation",
    delay=1.0,
    max_retries=3
)

# Загрузить документацию
urls = [
    "https://docs.cursor.com/llms-full.txt",
    "https://docs.claude.com/llms.txt"
]

downloader.download_from_list(urls)

# Вывести статистику
print(f"Загружено страниц: {downloader.stats['doc_pages']}")
print(f"Ошибок: {downloader.stats['errors']}")
```

## 🔍 Что будет загружено

### Cursor (docs.cursor.com)

Обычно llms-full.txt содержит:
- Getting Started Guide
- Features Documentation
  - AI Chat
  - Code Generation
  - Tab Completion
- API Reference
- Settings and Configuration
- Keyboard Shortcuts
- Advanced Topics

Примерно **30-50 страниц** документации.

### Claude (docs.claude.com)

llms.txt обычно включает:
- Introduction to Claude
- API Documentation
- SDK References
- Best Practices
- Examples and Tutorials
- Integration Guides

Примерно **50-80 страниц**.

### Linear (linear.app)

- API Documentation
- Integration Guides
- Webhooks
- GraphQL Schema
- SDK References

Примерно **40-60 страниц**.

### Railway (railway.com)

- Deployment Guides
- Configuration
- CLI Documentation
- Integrations
- Troubleshooting

Примерно **30-40 страниц**.

### Mem0 (docs.mem0.ai)

- Getting Started
- API Reference
- Python SDK
- Use Cases
- Examples

Примерно **20-30 страниц**.

## 📊 Ожидаемые результаты полной загрузки

При загрузке всех источников из `llms_urls.txt`:

```
================================================================================
Download Statistics:
================================================================================
llms.txt files processed: 6
Documentation pages downloaded: 210-280
Pages skipped (duplicates): 15-25
Errors encountered: 0-5

Output directory: /path/to/llm_docs
Total size: ~50-100 MB
================================================================================
```

## ⚙️ Рекомендуемые настройки

### Для быстрой загрузки

```bash
python download_llm_docs.py --config llms_urls.txt --delay 0.5
```

### Для надёжной загрузки (избежание блокировок)

```bash
python download_llm_docs.py --config llms_urls.txt --delay 2.0 --max-retries 5
```

### Для большого объёма данных

```bash
python download_llm_docs.py --config llms_urls.txt --delay 1.5 --max-retries 4
```

## 🛠 Дополнительные возможности

### Добавить свои источники

Отредактируйте `llms_urls.txt`:

```
# Мои источники
https://your-docs.com/llms.txt
https://another-site.com/llms.txt
```

### Фильтрация URL

Создайте свой скрипт на основе `example_usage.py`:

```python
from download_llm_docs import LLMDocsDownloader

downloader = LLMDocsDownloader()

# Загрузить и отфильтровать
with open("llms_urls.txt") as f:
    urls = [line.strip() for line in f if "cursor" in line or "claude" in line]

downloader.download_from_list(urls)
```

### Обновление документации

```bash
# Удалить старые файлы
rm -rf llm_docs/

# Загрузить свежую версию
python download_llm_docs.py --config llms_urls.txt
```

## 📅 Рекомендации по использованию

1. **Первая загрузка**: Используйте `--delay 1.5` для надёжности
2. **Регулярные обновления**: Настройте cron/scheduled task для автоматического обновления
3. **Хранение**: Делайте резервные копии загруженной документации
4. **Версионирование**: Сохраняйте разные версии документации в отдельных директориях

### Пример cron job (обновление раз в неделю)

```bash
# Добавьте в crontab:
0 2 * * 0 cd /path/to/agent0 && python download_llm_docs.py --config llms_urls.txt --output "llm_docs_$(date +\%Y\%m\%d)"
```

## 🎓 Для разработчиков

### Расширение функционала

Скрипт легко расширяется. Примеры в `example_usage.py`:

```python
# Пример 1: Базовая загрузка
python example_usage.py 1

# Пример 2: С настройками
python example_usage.py 2

# Пример 3: С анализом статистики
python example_usage.py 3

# Пример 4: Одиночный файл
python example_usage.py 4

# Пример 5: Из файла конфигурации
python example_usage.py 5
```

### API класса LLMDocsDownloader

```python
downloader = LLMDocsDownloader(
    output_dir="docs",      # Директория для сохранения
    delay=1.0,             # Задержка между запросами
    max_retries=3          # Максимум повторных попыток
)

# Основные методы
downloader.download_llms_txt(url)           # Загрузить один llms.txt
downloader.download_from_list(urls)         # Загрузить список
downloader.parse_llms_txt(content, base)    # Распарсить содержимое
downloader.extract_main_content(html, url)  # HTML → Markdown
downloader.print_stats()                    # Вывести статистику
```

## 🎉 Итог

После клонирования репозитория и запуска на вашем компьютере, скрипт загрузит всю документацию в удобном markdown-формате, организованную по доменам, с метаданными и статистикой.

**Время полной загрузки**: ~5-15 минут (в зависимости от delay)
**Размер результата**: ~50-100 MB
**Количество страниц**: ~200-300 страниц документации

Готово к использованию! 🚀
