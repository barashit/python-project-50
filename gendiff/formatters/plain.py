def format_plain(diff):
    """Форматирует вывод в виде plain текста."""

    def recurse(diff, parent_key=''):
        """Рекурсивно обрабатывает diff и генерирует строки для вывода."""
        result = []
        for item in diff:
            key = item['key']
            value = item.get('value')
            old_value = item.get('old_value')
            status = item['status']

            full_key = f"{parent_key}.{key}" if parent_key else key

            if status == 'added':
                result.append(f"Property '{full_key}' was added with value: {format_value(value)}")
            elif status == 'removed':
                result.append(f"Property '{full_key}' was removed")
            elif status == 'updated':
                result.append(f"Property '{full_key}' was updated. From {format_value(old_value)} to {format_value(value)}")
            elif status == 'unchanged':
                continue
            elif status == 'nested':
                result.extend(recurse(item['children'], full_key))

        return result

    def format_value(value):
        """Форматирует значение в зависимости от типа."""
        if isinstance(value, dict):
            return '[complex value]'
        elif isinstance(value, str):
            return f"'{value}'"
        return str(value)

    return "\n".join(recurse(diff))

