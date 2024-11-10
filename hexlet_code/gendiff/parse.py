# hexlet_code/gendiff/parse.py

import json
import yaml
import os

def read_file(file_path):
    """Читает и парсит JSON или YAML файл в зависимости от расширения."""
    _, ext = os.path.splitext(file_path)
    
    if ext == '.json':
        return read_json_file(file_path)
    elif ext in ['.yml', '.yaml']:
        return read_yaml_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def read_json_file(file_path):
    """Читает и парсит JSON файл."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{file_path}' не является корректным JSON.")
        exit(1)

def read_yaml_file(file_path):
    """Читает и парсит YAML файл."""
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        exit(1)
    except yaml.YAMLError:
        print(f"Ошибка: Файл '{file_path}' не является корректным YAML.")
        exit(1)

