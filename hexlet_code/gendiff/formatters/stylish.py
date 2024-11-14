def format_stylish(diff):
    """Форматирует вывод в виде stylish текста."""

    def recurse(diff, level=0):
        """Рекурсивно обрабатывает diff и добавляет отступы для вложенных объектов."""
        result = []
        indent = "  " * level
        for item in diff:
            key = item['key']
            value = item.get('value')
            old_value = item.get('old_value')
            status = item['status']


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
                result.extend(recurse(item['children'], level + 1))
                result.append(f"{indent}  }}")

        return result

    def format_value(value):
        """Форматирует значение в зависимости от типа."""
        if isinstance(value, dict):
            return '{'
        elif isinstance(value, str):
            return f"'{value}'"
        return str(value)


    return "\n".join(recurse(diff))

