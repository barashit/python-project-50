import pytest
import json
import os
import sys
import typing

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gendiff')))
print(sys.path)  
from gendiff.generate_diff import generate_diff

@pytest.fixture
def json_file_1():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    return fixture_path


@pytest.fixture
def json_file_2():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    return fixture_path


@pytest.mark.parametrize('format', ['json', 'plain', 'stylish'])
def test_generate_diff(format):
    file_path1 = os.path.join(os.path.dirname(__file__), 'fixtures', f'file1.{format}')
    file_path2 = os.path.join(os.path.dirname(__file__), 'fixtures', f'file2.{format}')

    assert isinstance(generate_diff, typing.Callable), 'gendiff.generate_diff must be function'
    
    result = generate_diff(file_path1, file_path2, format_name=format)

    if format == 'json':
        expected_result = [
            {"key": "common", "status": "nested", "children": [
                {"key": "follow", "value": False, "status": "added"},
                {"key": "setting1", "value": "Value 1", "status": "unchanged"},
                {"key": "setting2", "value": 200, "status": "removed"},
                {"key": "setting3", "old_value": True, "value": None, "status": "updated"},
                {"key": "setting4", "value": "blah blah", "status": "added"},
                {"key": "setting5", "value": {"key5": "value5"}, "status": "added"},
                {"key": "setting6", "status": "nested", "children": [
                    {"key": "doge", "status": "nested", "children": [
                        {"key": "wow", "old_value": "", "value": "so much", "status": "updated"}
                    ]},
                    {"key": "key", "value": "value", "status": "unchanged"},
                    {"key": "ops", "value": "vops", "status": "added"}
                ]}
            ]},
            {"key": "group1", "status": "nested", "children": [
                {"key": "baz", "old_value": "bas", "value": "bars", "status": "updated"},
                {"key": "foo", "value": "bar", "status": "unchanged"},
                {"key": "nest", "old_value": {"key": "value"}, "value": "str", "status": "updated"}
            ]},
            {"key": "group2", "value": {"abc": 12345, "deep": {"id": 45}}, "status": "removed"},
            {"key": "group3", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}, "status": "added"}
        ]

        assert json.loads(result) == expected_result

    elif format == 'plain':
        expected_diff = (
            "Property 'common.follow' was added with value: False\n"
            "Property 'common.setting2' was removed\n"
            "Property 'common.setting3' was updated. From True to None\n"
            "Property 'common.setting4' was added with value: 'blah blah'\n"
            "Property 'common.setting5' was added with value: [complex value]\n"
            "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
            "Property 'common.setting6.ops' was added with value: 'vops'\n"
            "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
            "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
            "Property 'group2' was removed\n"
            "Property 'group3' was added with value: [complex value]"
        )

        assert result.strip().lower() == expected_diff.strip().lower()

    elif format == 'stylish':
        expected_stylish_diff = (
            "{\n"
            "  common: {\n"
            "    follow: false  # added\n"
            "    setting1: Value 1  # unchanged\n"
            "    setting2: 200  # removed\n"
            "    setting3: true  # updated\n"
            "    setting4: blah blah  # added\n"
            "    setting5: {key5: value5}  # added\n"
            "    setting6: {\n"
            "      doge: {\n"
            "        wow: so much  # updated\n"
            "      }\n"
            "      key: value  # unchanged\n"
            "      ops: vops  # added\n"
            "    }\n"
            "  }\n"
            "  group1: {\n"
            "    baz: bars  # updated\n"
            "    foo: bar  # unchanged\n"
            "    nest: str  # updated\n"
            "  }\n"
            "  group2: {abc: 12345, deep: {id: 45}}  # removed\n"
            "  group3: {deep: {id: {number: 45}}, fee: 100500}  # added\n"
            "}\n"
        )

        assert result.strip() == expected_stylish_diff.strip()

