# tests/test_generate_diff.py

import pytest
import json
import yaml
from hexlet_code.gendiff.generate_diff import generate_diff


@pytest.fixture
def json_file_1(tmpdir):
    data = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    file_path = tmpdir.join("file1.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)


@pytest.fixture
def json_file_2(tmpdir):
    data = {
        "key1": "value1",
        "key2": "value2",
        "key4": "value4"
    }
    file_path = tmpdir.join("file2.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)


@pytest.fixture
def yaml_file_1(tmpdir):
    data = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    file_path = tmpdir.join("file1.yml")
    with open(file_path, 'w') as f:
        yaml.dump(data, f)
    return str(file_path)


@pytest.fixture
def yaml_file_2(tmpdir):
    data = {
        "key1": "value1",
        "key2": "value2",
        "key4": "value4"
    }
    file_path = tmpdir.join("file2.yml")
    with open(file_path, 'w') as f:
        yaml.dump(data, f)
    return str(file_path)


def test_identical_json_files(json_file_1):
    diff = generate_diff(json_file_1, json_file_1)
    expected_diff = """
  key1: value1
  key2: value2
  key3: value3
"""
    assert diff.strip() == expected_diff.strip()


def test_added_key(json_file_1, json_file_2):
    diff = generate_diff(json_file_1, json_file_2)
    expected_diff = """
  key1: value1
  key2: value2
  - key3: value3
  + key4: value4
"""
    assert diff.strip() == expected_diff.strip()


def test_identical_yaml_files(yaml_file_1):
    diff = generate_diff(yaml_file_1, yaml_file_1)
    expected_diff = """
  key1: value1
  key2: value2
  key3: value3
"""
    assert diff.strip() == expected_diff.strip()


def test_added_key_yaml(yaml_file_1, yaml_file_2):
    diff = generate_diff(yaml_file_1, yaml_file_2)
    expected_diff = """
  key1: value1
  key2: value2
  - key3: value3
  + key4: value4
"""
    assert diff.strip() == expected_diff.strip()

