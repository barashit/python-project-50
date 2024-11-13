# hexlet_code/gendiff/generate_diff.py

from hexlet_code.gendiff.parse import read_file  # Импортируем функцию для чтения файлов
from hexlet_code.gendiff.formatters.stylish import format_stylish  # Импортируем форматирование для stylish
from hexlet_code.gendiff.formatters.plain import format_plain  # Импортируем форматирование для plain

def generate_diff(file1, file2, format_name='stylish'):
    """Генерирует дифф между двумя JSON или YAML файлами."""

    # Чтение и парсинг данных из файлов
    data1 = read_file(file1)
    data2 = read_file(file2)

    # Получаем все уникальные ключи из обоих файлов
    keys = sorted(set(data1.keys()).union(data2.keys()))

    diff_result = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Если значения одинаковые
        if value1 == value2:
            diff_result.append({'key': key, 'value': value1, 'status': 'unchanged'})
        
        # Если ключ есть в data1, но нет в data2
        elif key in data1 and key not in data2:
            diff_result.append({'key': key, 'value': value1, 'status': 'removed'})
        
        # Если ключ есть в data2, но нет в data1
        elif key not in data1 and key in data2:
            diff_result.append({'key': key, 'value': value2, 'status': 'added'})
        
        # Если значения различаются
        else:
            # Если оба значения являются вложенными объектами (словарями)
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2)  # Рекурсивно обрабатываем вложенные объекты
                })
            else:
                diff_result.append({'key': key, 'old_value': value1, 'value': value2, 'status': 'updated'})

    # В зависимости от формата, возвращаем результат
    if format_name == 'plain':
        return format_plain(diff_result)  # Вызываем format_plain для форматирования
    elif format_name == 'stylish':
        return format_stylish(diff_result)  # Вызываем format_stylish для форматирования
    else:
        raise ValueError(f"Unknown format: {format_name}")  # Если неизвестный формат, выбрасываем исключение

def generate_diff_recursive(data1, data2):
    """Рекурсивно генерирует дифф для вложенных объектов (словарей)."""
    keys = sorted(set(data1.keys()).union(data2.keys()))  # Получаем все ключи из обоих объектов
    diff_result = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Если значения одинаковые
        if value1 == value2:
            diff_result.append({'key': key, 'value': value1, 'status': 'unchanged'})
        
        # Если ключ есть в data1, но нет в data2
        elif key in data1 and key not in data2:
            diff_result.append({'key': key, 'value': value1, 'status': 'removed'})
        
        # Если ключ есть в data2, но нет в data1
        elif key not in data1 and key in data2:
            diff_result.append({'key': key, 'value': value2, 'status': 'added'})
        
        # Если значения различаются
        else:
            # Если оба значения являются вложенными объектами (словарями)
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff_result.append({
                    'key': key,
                    'status': 'nested',
                    'children': generate_diff_recursive(value1, value2)  # Рекурсивно вызываем для вложенных объектов
                })
            else:
                diff_result.append({'key': key, 'old_value': value1, 'value': value2, 'status': 'updated'})

    return diff_result  # Возвращаем результат рекурсивного диффа

