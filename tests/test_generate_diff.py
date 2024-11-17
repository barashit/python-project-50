import pytest
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hexlet_code')))
print(sys.path)  
from hexlet_code.gendiff.generate_diff import generate_diff

@pytest.fixture
def json_file_1():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    return fixture_path


@pytest.fixture
def json_file_2():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    return fixture_path


def test_generate_diff_json(json_file_1, json_file_2):
    # Ожидаемый результат в JSON формате
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
    
    # Получаем результат в формате JSON
    result = generate_diff(json_file_1, json_file_2, format_name='json')

    # Сравниваем результат с ожидаемым
    assert json.loads(result) == expected_result


# в формате plain
def test_plain_diff(json_file_1, json_file_2):
    diff = generate_diff(json_file_1, json_file_2, 'plain')
    print(f"Generated diff:\n{diff}")

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

    assert diff.strip().lower() == expected_diff.strip().lower()


# YAML
def test_generate_diff_yaml():
    yaml_file_1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
    yaml_file_2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')

    # Ожидаемый результат 
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
    

    result = generate_diff(yaml_file_1, yaml_file_2, format_name='json')


    assert json.loads(result) == expected_result

