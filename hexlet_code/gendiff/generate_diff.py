import json

def read_file(file_path):
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

def generate_diff(file1, file2):
    """Генерирует дифф между двумя JSON-файлами."""
    # Чтение и парсинг данных из файлов
    data1 = read_file(file1)
    data2 = read_file(file2)
    
    # Получение всех уникальных ключей из обоих файлов
    keys = sorted(set(data1.keys()).union(data2.keys()))

    diff_result = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            # Если значения одинаковые, просто выводим ключ с его значением
            diff_result.append(f"  {key}: {value1}")
        elif key in data1 and key not in data2:
            # Если ключ есть в data1, но нет в data2, выводим его с минусом
            diff_result.append(f"  - {key}: {value1}")
        elif key not in data1 and key in data2:
            # Если ключ есть в data2, но нет в data1, выводим его с плюсом
            diff_result.append(f"  + {key}: {value2}")
        else:
            # Если значения различаются, выводим их с минусом и плюсом
            diff_result.append(f"  - {key}: {value1}")
            diff_result.append(f"  + {key}: {value2}")

    return "\n".join(diff_result)

