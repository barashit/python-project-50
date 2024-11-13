import pytest
import json
import yaml
from hexlet_code.gendiff.generate_diff import generate_diff
import os


# Фикстуры для загрузки JSON файлов из директории fixtures
@pytest.fixture
def json_file_1():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    with open(fixture_path, 'r') as f:
        return json.load(f)


@pytest.fixture
def json_file_2():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    with open(fixture_path, 'r') as f:
        return json.load(f)


# Фикстуры для загрузки YAML файлов из директории fixtures
@pytest.fixture
def yaml_file_1():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
    with open(fixture_path, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture
def yaml_file_2():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')
    with open(fixture_path, 'r') as f:
        return yaml.safe_load(f)


# Тесты для проверки различий между JSON файлами
def test_generate_diff_json(json_file_1, json_file_2):
    diff = generate_diff(json_file_1, json_file_2)
    expected_diff = """
  common: {
    setting1: Value 1
  - setting2: 200
  + setting4: blah blah
    setting3: null
  + setting5: {
        key5: value5
      }
    follow: false
    setting6: {
      key: value
      ops: vops
      doge: {
        wow: so much
      }
    }
  }
  group1: {
  - baz: bas
  + baz: bars
    foo: bar
  - nest: {
        key: value
      }
  + nest: str
  }
  - group2: {
      abc: 12345
      deep: {
        id: 45
      }
    }
  + group3: {
      deep: {
        id: {
          number: 45
        }
      }
      fee: 100500
    }
}
"""
    assert diff.strip() == expected_diff.strip()


# Тесты для проверки различий между YAML файлами
def test_generate_diff_yaml(yaml_file_1, yaml_file_2):
    diff = generate_diff(yaml_file_1, yaml_file_2)
    expected_diff = """
  common: {
    setting1: Value 1
  - setting2: 200
  + setting4: blah blah
    setting3: null
  + setting5: {
        key5: value5
      }
    follow: false
    setting6: {
      key: value
      ops: vops
      doge: {
        wow: so much
      }
    }
  }
  group1: {
  - baz: bas
  + baz: bars
    foo: bar
  - nest: {
        key: value
      }
  + nest: str
  }
  - group2: {
      abc: 12345
      deep: {
        id: 45
      }
    }
  + group3: {
      deep: {
        id: {
          number: 45
        }
      }
      fee: 100500
    }
}
"""
    assert diff.strip() == expected_diff.strip()



@pytest.fixture
def json_file_1(tmpdir):
    data = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        }
    }
    file_path = tmpdir.join("file1.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)


@pytest.fixture
def json_file_2(tmpdir):
    data = {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
    file_path = tmpdir.join("file2.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)


def test_plain_diff(json_file_1, json_file_2):
    diff = generate_diff(json_file_1, json_file_2, 'plain')
    expected_diff = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to null\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )
    assert diff.strip() == expected_diff.strip()


