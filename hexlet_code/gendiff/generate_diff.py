# hexlet_code/gendiff/generate_diff.py

from hexlet_code.gendiff.parse import read_file
from hexlet_code.gendiff.formatters.stylish import stylish  # Импортируем форматер stylish

def generate_diff(file1, file2, format_name='stylish'):
    """Генерирует дифф между двумя JSON или YAML файлами и форматирует его согласно указанному формату."""
    # Чтение и парсинг данных из файлов
    data1 = read_file(file1)
    data2 = read_file(file2)

    # Получаем все уникальные ключи из обоих файлов
    keys = sorted(set(data1.keys()).union(data2.keys()))

    # Построение промежуточного представления диффа
    diff_result = {}

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff_result[key] = (value1, value2)
        elif key in data1 and key not in data2:
            diff_result[key] = (value1, None)  # Удалено
        elif key not in data1 and key in data2:
            diff_result[key] = (None, value2)  # Добавлено
        else:
            diff_result[key] = (value1, value2)  # Изменено

    # Если формат не указан, по умолчанию используем 'stylish'
    if format_name == 'stylish':
        return stylish(diff_result)
    else:
        raise ValueError(f"Unsupported format: {format_name}")

