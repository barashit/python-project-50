import json
import yaml
import os

def read_file(file_path):
    """Читает файл и возвращает данные в виде Python объекта."""
    _, ext = os.path.splitext(file_path)
    if ext == '.json':
        with open(file_path, 'r') as f:
            return json.load(f)
    elif ext == '.yml' or ext == '.yaml':
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

