from gendiff.parse import read_file
from gendiff.formatters import format_stylish, format_plain, format_json
import json
import re

def generate_diff(file1, file2, format_name='stylish'):
    """Генерирует дифф между двумя JSON или YAML файлами."""
    
    data1 = read_file(file1)
    data2 = read_file(file2)

    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff_result = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'unchanged'})
        
        elif key in data1 and key not in data2:
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'removed'})
        
        elif key not in data1 and key in data2:
            diff_result.append({'key': key, 'value': format_value(value2, format_name), 'status': 'added'})
        
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2, format_name)
                })
            else:
                diff_result.append({'key': key, 'old_value': format_value(value1, format_name), 'value': format_value(value2, format_name), 'status': 'updated'})

    if format_name == 'plain':
        return format_plain(diff_result)  # plain
    elif format_name == 'stylish':
        return format_stylish(diff_result)  # stylish
    elif format_name == 'json':
        return format_json(diff_result)  # json
    else:
        raise ValueError(f"Unknown format: {format_name}")  # Если формат неизвестен

def generate_diff_recursive(data1, data2, format_name):
    """Рекурсивно генерирует дифф для вложенных словарей."""
    keys = sorted(set(data1.keys()).union(data2.keys()))  # Получаем все уникальные ключи
    diff_result = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'unchanged'})
        
        elif key in data1 and key not in data2:
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'removed'})
        
        elif key not in data1 and key in data2:
            diff_result.append({'key': key, 'value': format_value(value2, format_name), 'status': 'added'})
        
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2, format_name)
                })
            else:
                diff_result.append({'key': key, 'old_value': format_value(value1, format_name), 'value': format_value(value2, format_name), 'status': 'updated'})

    return diff_result

def format_value(value, format_name):
    if value == 'null':
        value = None

    if value is None:
        return 'null' if format_name in ['json', 'stylish'] else 'null'
    
    elif isinstance(value, bool):
        if format_name == 'plain':
            return 'true' if value else 'false'
        return value
    
    elif isinstance(value, str):
        return value

    return value


def normalize_result(result: str):
    normalized_result = " ".join(result.strip().split())
    normalized_result = re.sub(r"'", '"', normalized_result)
    normalized_result = re.sub(r"\bnull\b", "null", normalized_result)
    return normalized_result
