import json

def format_json(diff):
    """Форматирует дифф в формате JSON."""

    return json.dumps(diff, indent=2)

