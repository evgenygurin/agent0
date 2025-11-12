# Troubleshooting / Решение проблем

## Ошибка 403 Forbidden

### Проблема

```
Error fetching https://docs.cursor.com/llms-full.txt: 403 Client Error: Forbidden
```

### Причины

1. **Ограничения песочницы** - Некоторые окружения (Docker, CI/CD, песочницы) блокируют внешние HTTP запросы
2. **Защита от ботов** - Сайт блокирует автоматические запросы
3. **Rate limiting** - Слишком много запросов за короткое время
4. **Геоблокировка** - Сайт недоступен из вашего региона
5. **User-Agent фильтрация** - Сайт требует специфичный User-Agent

### Решения

#### 1. Увеличить задержку между запросами

```bash
python download_llm_docs.py --config llms_urls.txt --delay 2.0
```

#### 2. Изменить User-Agent

Отредактируйте `download_llm_docs.py`, строка ~48:

```python
self.session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})
```

#### 3. Использовать прокси

```python
# В конструкторе LLMDocsDownloader
self.session.proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'http://proxy.example.com:8080',
}
```

#### 4. Добавить дополнительные заголовки

```python
self.session.headers.update({
    'User-Agent': 'Mozilla/5.0 ...',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
})
```

#### 5. Использовать браузер для ручной загрузки

Если автоматическая загрузка не работает:

```bash
# 1. Откройте URL в браузере
# 2. Сохраните страницу как llms.txt
# 3. Обработайте локальный файл:

python -c "
from download_llm_docs import LLMDocsDownloader
with open('llms.txt', 'r') as f:
    content = f.read()
downloader = LLMDocsDownloader()
parsed = downloader.parse_llms_txt(content, 'https://docs.example.com/llms.txt')
print(f'Found {len(parsed[\"urls\"])} URLs')
"
```

#### 6. Использовать curl с cookies

```bash
# Получить cookies через браузер, затем:
curl -H "User-Agent: Mozilla/5.0..." \
     -H "Cookie: session=abc123..." \
     https://docs.cursor.com/llms-full.txt > llms.txt
```

## Тестирование в песочнице

Если вы находитесь в ограниченной среде (например, Docker, CI/CD), используйте демо-скрипт:

```bash
python demo_llms_downloader.py
```

Этот скрипт показывает все возможности парсера без реальных HTTP запросов.

## Проверка доступности URL

Перед запуском основного скрипта проверьте доступность:

```bash
# Простая проверка
curl -I https://docs.cursor.com/llms-full.txt

# С User-Agent
curl -I -A "Mozilla/5.0" https://docs.cursor.com/llms-full.txt

# С verbose выводом
curl -v https://docs.cursor.com/llms-full.txt
```

## Альтернативные методы загрузки

### Использование requests с сессией браузера

Установите `requests_html` или `selenium` для эмуляции браузера:

```bash
pip install requests-html
```

```python
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://docs.cursor.com/llms-full.txt')
print(r.text)
```

### Использование wget

```bash
wget --user-agent="Mozilla/5.0" \
     --wait=1 \
     --random-wait \
     -r -l 1 \
     https://docs.cursor.com/llms-full.txt
```

## Работа с локальными копиями

Если у вас уже есть локальные копии llms.txt файлов:

```bash
# Создайте локальную структуру
mkdir -p local_llms_files

# Скопируйте файлы
cp cursor-llms.txt local_llms_files/
cp claude-llms.txt local_llms_files/

# Обработайте локально
python process_local_llms.py local_llms_files/
```

Пример `process_local_llms.py`:

```python
#!/usr/bin/env python3
import os
from pathlib import Path
from download_llm_docs import LLMDocsDownloader

def process_local_files(directory):
    downloader = LLMDocsDownloader(output_dir="local_docs")

    for filepath in Path(directory).glob("*.txt"):
        print(f"Processing {filepath}")
        with open(filepath, 'r') as f:
            content = f.read()

        parsed = downloader.parse_llms_txt(
            content,
            f"file://{filepath.absolute()}"
        )

        print(f"Found {len(parsed['urls'])} URLs")
        # Дальнейшая обработка...

if __name__ == "__main__":
    import sys
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    process_local_files(directory)
```

## Логирование и отладка

Включите детальное логирование:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Теперь requests будет выводить детальную информацию
```

## Проблемы с SSL/TLS

Если возникают ошибки сертификатов:

```python
# ВНИМАНИЕ: Только для тестирования! Небезопасно!
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get(url, verify=False)
```

Лучший вариант - обновить сертификаты:

```bash
pip install --upgrade certifi
```

## Получение помощи

Если проблема не решается:

1. Проверьте, доступен ли сайт через обычный браузер
2. Убедитесь, что у вас есть интернет-соединение
3. Попробуйте другой сайт из списка
4. Запустите demo_llms_downloader.py для проверки работы парсера
5. Создайте issue на GitHub с деталями ошибки

## Полезные команды для диагностики

```bash
# Проверка DNS
nslookup docs.cursor.com

# Проверка подключения
ping docs.cursor.com

# Проверка портов
telnet docs.cursor.com 443

# Трассировка маршрута
traceroute docs.cursor.com

# Проверка через curl с деталями
curl -v -L https://docs.cursor.com/llms-full.txt 2>&1 | head -50
```

## Рекомендации для production

1. **Кэширование** - Сохраняйте загруженные файлы для повторного использования
2. **Rate Limiting** - Используйте задержку минимум 1 секунда между запросами
3. **Retry Logic** - Реализуйте экспоненциальную задержку (уже есть в скрипте)
4. **Мониторинг** - Логируйте все ошибки для анализа
5. **Резервные копии** - Сохраняйте предыдущие версии документации
6. **Уважайте robots.txt** - Проверяйте правила сайта

## Лицензионные ограничения

Перед массовой загрузкой документации:

1. Проверьте terms of service сайта
2. Убедитесь, что разрешено автоматическое скачивание
3. Соблюдайте авторские права
4. Используйте данные только для разрешённых целей
