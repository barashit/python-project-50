import pytest
import json
from gendiff.generate_diff import generate_diff


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
    return file_path


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
    return file_path


@pytest.fixture
def json_file_identical(tmpdir):
    data = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    file_path = tmpdir.join("file_identical.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path


def test_identical_json_files(json_file_identical):
    diff = generate_diff(str(json_file_identical), str(json_file_identical))
    expected_diff = """
  key1: value1
  key2: value2
  key3: value3
"""
    assert diff.strip() == expected_diff.strip()


def test_added_key(json_file_1, json_file_2):
    diff = generate_diff(str(json_file_1), str(json_file_2))
    expected_diff = """
  key1: value1
  key2: value2
  - key3: value3
  + key4: value4
"""
    assert diff.strip() == expected_diff.strip()


def test_removed_key(json_file_1, json_file_2):
    diff = generate_diff(str(json_file_2), str(json_file_1))
    expected_diff = """
  key1: value1
  key2: value2
  - key4: value4
  + key3: value3
"""
    assert diff.strip() == expected_diff.strip()


def test_different_values(json_file_1, json_file_2):
    diff = generate_diff(str(json_file_1), str(json_file_2))
    expected_diff = """
  key1: value1
  key2: value2
  - key3: value3
  + key4: value4
"""
    assert diff.strip() == expected_diff.strip()

