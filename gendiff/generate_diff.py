from gendiff.parse import read_file
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json

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
            diff_result.append({'key': key, 'value': value1, 'status': 'unchanged'})
        
        elif key in data1 and key not in data2:
            diff_result.append({'key': key, 'value': value1, 'status': 'removed'})
        
        elif key not in data1 and key in data2:
            diff_result.append({'key': key, 'value': value2, 'status': 'added'})
        
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2)
                })
            else:
                diff_result.append({'key': key, 'old_value': value1, 'value': value2, 'status': 'updated'})

    # В зависимости от формата
    if format_name == 'plain':
        return format_plain(diff_result)  #plain
    elif format_name == 'stylish':
        return format_stylish(diff_result)  #stylish
    elif format_name == 'json':
        return format_json(diff_result)  #json
    else:
        raise ValueError(f"Unknown format: {format_name}")  # Если формат неизвестен


def generate_diff_recursive(data1, data2):
    keys = sorted(set(data1.keys()).union(data2.keys()))  # Получаем ключи
    diff_result = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff_result.append({'key': key, 'value': value1, 'status': 'unchanged'})
        
        elif key in data1 and key not in data2:
            diff_result.append({'key': key, 'value': value1, 'status': 'removed'})
        
        elif key not in data1 and key in data2:
            diff_result.append({'key': key, 'value': value2, 'status': 'added'})
        
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2)
                })
            else:
                diff_result.append({'key': key, 'old_value': value1, 'value': value2, 'status': 'updated'})

    return diff_result

