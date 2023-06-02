import os
from sys import argv

import pytest

from toolbox.utils._path_helper import get_abs_path
from toolbox.utils._reader import ReadFile
from toolbox.utils._parser import parse_unknown_args

##### FIXTURES #####
@pytest.fixture
def yml_path():
    return 'tests/conf/logging_config.yml'

##### TESTS #####

### utils/_path_helper.py ###
def test_get_abs_path():
    path = 'foo'
    assert get_abs_path(path) == os.path.join(os.path.dirname(argv[0]), path)

### utils/_reader.py ###
class TestReadFile:
    @staticmethod
    def test_yml(yml_path):
        assert isinstance(ReadFile.yml(yml_path), dict or list)

### utils/_parser.py ###
def test_parse_unknown_args():
    args = [
            "test",
            "--foo",
            "bar",
            "-buz",
            "1",
            "2",
            "3",
            "--sys",
            "xyz"
            ]
    target = {
              "unnamed": "test",
              "foo": "bar",
              "buz": [
                  "1",
                  "2",
                  "3"
              ],
              "sys": "xyz"
              }
    assert parse_unknown_args(args=args, prefix="-") == target