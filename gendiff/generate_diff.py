from gendiff.parse import read_file
from gendiff.formatters import format_stylish, format_plain, format_json
import json
import re

def generate_diff(file1, file2, format_name='stylish'):
    """Генерирует дифф между двумя JSON или YAML файлами."""
    
    # Чтение данных из файлов
    data1 = read_file(file1)
    data2 = read_file(file2)

    # Получаем все уникальные ключи
    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff_result = []

    # Обрабатываем каждый ключ
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            # Если значения одинаковые
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'unchanged'})
        
        elif key in data1 and key not in data2:
            # Если ключ есть в первом файле, но нет во втором
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'removed'})
        
        elif key not in data1 and key in data2:
            # Если ключ есть во втором файле, но нет в первом
            diff_result.append({'key': key, 'value': format_value(value2, format_name), 'status': 'added'})
        
        else:
            # Если значения разные, проверяем на вложенные структуры
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2, format_name)
                })
            else:
                diff_result.append({'key': key, 'old_value': format_value(value1, format_name), 'value': format_value(value2, format_name), 'status': 'updated'})

    # Возвращаем результат в нужном формате
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
            # Если значения одинаковые
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'unchanged'})
        
        elif key in data1 and key not in data2:
            # Если ключ есть в первом файле, но нет во втором
            diff_result.append({'key': key, 'value': format_value(value1, format_name), 'status': 'removed'})
        
        elif key not in data1 and key in data2:
            # Если ключ есть во втором файле, но нет в первом
            diff_result.append({'key': key, 'value': format_value(value2, format_name), 'status': 'added'})
        
        else:
            # Если значения разные, проверяем на вложенные структуры
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
    """Форматирует значения для корректного вывода в YAML/JSON."""
    if value is None:
        # Для JSON и других форматов 'null' без кавычек
        if format_name == 'json' or format_name == 'stylish':
            return 'null'
        return 'null'  # Для plain тоже заменяем на 'null'
    
    elif isinstance(value, bool):
        # Для plain форматируем True/False в строку 'true'/'false'
        if format_name == 'plain':
            return 'true' if value else 'false'
        return value  # Булевые значения остаются как есть (True/False) для JSON и Stylish
    
    elif isinstance(value, str):
        return value  # Строки выводятся как есть

    return value  # Для чисел и других типов просто возвращаем их

# Нормализация вывода для тестов
def normalize_result(result: str):
    # Убираем лишние пробелы и приводим строки в нижний регистр
    normalized_result = " ".join(result.strip().split())
    normalized_result = re.sub(r"'", '"', normalized_result)  # Преобразуем одинарные кавычки в двойные
    normalized_result = re.sub(r"\bnull\b", "null", normalized_result)  # Заменяем 'null' (строка) на null
    return normalized_result
