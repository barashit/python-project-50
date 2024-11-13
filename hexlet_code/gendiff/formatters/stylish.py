# hexlet_code/gendiff/formatters/stylish.py

def format_stylish(diff):
    """Форматирует вывод в виде stylish текста."""

    def recurse(diff, level=0):
        """Рекурсивно обрабатывает diff и добавляет отступы для вложенных объектов."""
        result = []
        indent = "  " * level  # Отступ для текущего уровня
        for item in diff:
            key = item['key']
            value = item.get('value')
            old_value = item.get('old_value')
            status = item['status']

            # Обработка различных состояний изменений
            if status == 'added':
                result.append(f"{indent}+ {key}: {format_value(value)}")
            elif status == 'removed':
                result.append(f"{indent}- {key}: {format_value(value)}")
            elif status == 'updated':
                result.append(f"{indent}- {key}: {format_value(old_value)}")
                result.append(f"{indent}+ {key}: {format_value(value)}")
            elif status == 'unchanged':
                result.append(f"{indent}  {key}: {format_value(value)}")
            elif status == 'nested':
                result.append(f"{indent}  {key}: {{")
                result.extend(recurse(item['children'], level + 1))  # Рекурсивно вызываем для вложенных объектов
                result.append(f"{indent}  }}")

        return result

    def format_value(value):
        """Форматирует значение в зависимости от типа."""
        if isinstance(value, dict):  # Если значение - это вложенный словарь, то показываем вложенные элементы
            return '{'  # Для словаря возвращаем открывающуюся фигурную скобку
        elif isinstance(value, str):  # Если строка, то оборачиваем в кавычки
            return f"'{value}'"
        return str(value)  # Для других типов (например, int, bool) просто выводим строковое представление

    # Возвращаем форматированный текст
    return "\n".join(recurse(diff))  # Рекурсивно обрабатываем все изменения

