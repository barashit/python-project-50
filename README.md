### Hexlet tests and linter status:
[![Actions Status](https://github.com/barashit/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/barashit/python-project-50/actions)

# Gendiff

Gendiff — утилита для сравнения двух конфигурационных файлов и вывода различий между ними. Программа поддерживает работу с файлами в формате JSON.

## Установка

Чтобы установить проект, используйте следующую команду:

```bash
pip install .


## Пример работы утилиты

[![asciicast](https://asciinema.org/a/687820.svg)](https://asciinema.org/a/687820)

### Пример 1: Сравнение двух JSON файлов

**data/file1.json**:
```json
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
