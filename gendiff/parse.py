import json
import yaml
import os

def normalize_data(data):
    if isinstance(data, dict):
        return {key: normalize_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [normalize_data(item) for item in data]
    elif isinstance(data, str):
        if data.lower() == 'true':
            return True
        elif data.lower() == 'false':
            return False
    return data

def read_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.json':
        with open(file_path, 'r') as f:
            data = json.load(f)
    elif ext == '.yml' or ext == '.yaml':
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
    
    return normalize_data(data)
