# gendiff/parse.py

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
    with open(file_path, 'r') as file:
        return json.load(file) 


def read_yaml_file(file_path):
    """Читает и парсит YAML файл."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
