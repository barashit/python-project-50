# hexlet_code/gendiff/formatters/stylish.py

def stylish_diff(value1, value2, depth=0):
    """Рекурсивно форматирует дифф между двумя значениями в формате 'stylish'."""
    indent = ' ' * (depth * 4)  # Отступ для уровня вложенности
    result = []

    if isinstance(value1, dict) and isinstance(value2, dict):
        # Если оба значения — словари, сравниваем их рекурсивно
        result.append("{")
        keys = sorted(set(value1.keys()).union(value2.keys()))  # Все уникальные ключи
        for key in keys:
            v1 = value1.get(key)
            v2 = value2.get(key)
            if v1 == v2:
                result.append(f"{indent}    {key}: {v1}")
            elif key not in value2:
                result.append(f"{indent}  - {key}: {v1}")
            elif key not in value1:
                result.append(f"{indent}  + {key}: {v2}")
            else:
                result.append(f"{indent}  - {key}: {v1}")
                result.append(f"{indent}  + {key}: {v2}")
        result.append(f"{indent}}}")
    elif value1 == value2:
        # Если значения одинаковые, выводим их
        result.append(f"{indent}  {value1}")
    else:
        # Если значения разные, выводим их с минусом и плюсом
        result.append(f"{indent}  - {value1}")
        result.append(f"{indent}  + {value2}")

    return result

def stylish(diff_result):
    """Форматирует и выводит весь дифф с учетом вложенных структур."""
    result = ['{']
    for key, (value1, value2) in diff_result.items():
        result.extend(stylish_diff(value1, value2, depth=1))
    result.append('}')
    return "\n".join(result)

