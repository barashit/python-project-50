import pytest
import json
import os
import sys
import typing
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gendiff')))
from gendiff.generate_diff import generate_diff

# Функция для нормализации различий в формате stylish
def normalize_stylish_diff(diff: str):
    # Преобразуем одинарные кавычки в двойные
    diff = re.sub(r"'", '"', diff)

    # Преобразуем значение null (строка или объект) без кавычек
    diff = re.sub(r"\bnull\b", "null", diff)

    # Убираем лишние пробелы между элементами
    diff = " ".join(diff.strip().split())

    # Преобразуем комментарии с добавлением / удалением значений
    diff = re.sub(r" # (added|removed|updated)", r" \1", diff)

    # Убираем пробелы после комментариев и на концах строк
    diff = re.sub(r"([a-zA-Z0-9]) #", r"\1#", diff)

    return diff

@pytest.mark.parametrize('format', ['json', 'plain', 'stylish'])
def test_generate_diff(format):
    # Используем правильные расширения для файлов
    file_path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')  # .json
    file_path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')  # .json

    assert isinstance(generate_diff, typing.Callable), 'gendiff.generate_diff must be function'

    result = generate_diff(file_path1, file_path2, format_name=format)

    class Child:
        def __init__(self, key, old_value, value, status, children):
            self.key = key
            self.old_v = old_value
            self.val = value
            self.stat = status
            self.kids = children
    if format == "json":
        c = Child("wow", "", "so much", "updated", [])
        doge_children = [
            {
                "key": c.key,
                "old_value": c.old_v,
                "value": c.val,
                "status": c.stat,
            },
        ]
        c1 = Child("doge", "", "", "nested", doge_children)
        c2 = Child("key", "", "value", "unchanged", [])
        c3 = Child("ops", "", "vops", "added", [])
        setting6_children = [
            {
                "key": c1.key,
                "status": c1.stat,
                "children": c1.kids,
            },
            {
                "key": c2.key,
                "value": c2.val,
                "status": c2.stat,
            },
            {
                "key": c3.key,
                "value": c3.val,
                "status": c3.stat,
            },
        ]

        c1 = Child("follow", "", False, "added", [])
        c2 = Child("setting1", "", "Value 1", "unchanged", [])
        c3 = Child("setting2", "", 200, "removed", [])
        c4 = Child("setting3", True, "null", "updated", [])
        c5 = Child("setting4", "", "blah blah", "added", [])
        c6 = Child("setting5", "", {"key5": "value5"}, "added", [])
        c7 = Child("setting6", "", "", "nested", setting6_children)
        common_children = [
            {
                "key": c1.key,
                "value": c1.val,
                "status": c1.stat,
            },
            {
                "key": c2.key,
                "value": c2.val,
                "status": c2.stat,
            },
            {
                "key": c3.key,
                "value": c3.val,
                "status": c3.stat,
            },
            {
                "key": c4.key,
                "old_value": c4.old_v,
                "value": c4.val,
                "status": c4.stat,
            },
            {
                "key": c5.key,
                "value": c5.val,
                "status": c5.stat,
            },
            {
                "key": c6.key,
                "value": c6.val,
                "status": c6.stat,
            },
            {
                "key": c7.key,
                "status": c7.stat,
                "children": c7.kids,
            },
        ]
        c1 = Child("baz", "bas", "bars", "updated", [])
        c2 = Child("foo", "", "bar", "unchanged", [])
        c3 = Child("nest", {"key": "value"}, "str", "updated", [])
        group1_children = [
            {
                "key": c1.key,
                "old_value": c1.old_v,
                "value": c1.val,
                "status": c1.stat,
            },
            {"key": c2.key, "value": c2.val, "status": c2.stat},
            {
                "key": c3.key,
                "old_value": c3.old_v,
                "value": c3.val,
                "status": c3.stat,
            },
        ]

        group2_val = {"abc": 12345, "deep": {"id": 45}}
        group3_val = {"deep": {"id": {"number": 45}}, "fee": 100500}
        c1 = Child("common", "", "", "nested", common_children)
        c2 = Child("group1", "", "", "nested", group1_children)
        c3 = Child("group2", "", group2_val, "removed", [])
        c4 = Child("group3", "", group3_val, "added", [])
        expected_result = [
            {
                "key": c1.key,
                "status": c1.stat,
                "children": c1.kids,
            },
            {
                "key": c2.key,
                "status": c2.stat,
                "children": c2.kids,
            },
            {
                "key": c3.key,
                "value": c3.val,
                "status": c3.stat,
            },
            {
                "key": c4.key,
                "value": c4.val,
                "status": c4.stat,
            },
        ]
        assert json.loads(result) == expected_result

    elif format == "plain":
        prop = [
            "Property 'common.follow'",
            "Property 'common.setting2'",
            "Property 'common.setting3'",
            "Property 'common.setting4'",
            "Property 'common.setting5'",
            "Property 'common.setting6.doge.wow'",
            "Property 'common.setting6.ops'",
            "Property 'group1.baz'",
            "Property 'group1.nest'",
            "Property 'group2'",
            "Property 'group3'",
        ]
        expected_diff = (
            f"{prop[0]} was added with value: false\n"
            f"{prop[1]} was removed\n"
            f"{prop[2]} was updated. From true to null\n"
            f"{prop[3]} was added with value: 'blah blah'\n"
            f"{prop[4]} was added with value: [complex value]\n"
            f"{prop[5]} was updated. From '' to 'so much'\n"
            f"{prop[6]} was added with value: 'vops'\n"
            f"{prop[7]} was updated. From 'bas' to 'bars'\n"
            f"{prop[8]} was updated. From [complex value] to 'str'\n"
            f"{prop[9]} was removed\n"
            f"{prop[10]} was added with value: [complex value]"
        )

        # Нормализуем результат и ожидаемый вывод
        def normalize(s: str) -> str:
            s = s.strip().lower().replace("'", "")
            s = s.replace("true", "true").replace("null", "null")
            return s
        result_normalized = normalize(result)
        expected_diff_normalized = normalize(expected_diff)

        assert result_normalized == expected_diff_normalized
