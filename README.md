### Hexlet tests and linter status:
[![Actions Status](https://github.com/barashit/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/barashit/python-project-50/actions)


[![hexlet-check](https://github.com/barashit/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/barashit/python-project-50/actions/workflows/hexlet-check.yml)


[![Code Climate Maintainability Badge](<a href="https://codeclimate.com/github/barashit/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b996bed1afa1cc203b55/test_coverage" /></a>)]


![Code Climate coverage](<a href="https://codeclimate.com/github/barashit/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b996bed1afa1cc203b55/test_coverage" /></a>)


# Gendiff

Этот инструмент позволяет сравнивать два файла в формате JSON или YAML и выводить различия между ними.

## Установка


## Установка

Чтобы установить проект, используйте следующую команду:

```bash
pip install .


## Пример работы утилиты

для файлов .json

[![asciicast](https://asciinema.org/a/687820.svg)](https://asciinema.org/a/687820)

для файлов .yml

[![asciicast](https://asciinema.org/a/688307.svg)](https://asciinema.org/a/688307)

### Пример 1: Сравнение двух JSON файлов

**data/file1.json**:
```json
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}


gendiff file1.yml file2.yml

