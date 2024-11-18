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
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON file {file_path}: {e}")
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file {file_path}: {e}")
        

def read_yaml_file(file_path):
    """Читает и парсит YAML файл."""
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file {file_path}: {e}")
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file {file_path}: {e}")

