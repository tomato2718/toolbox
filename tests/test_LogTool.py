import logging

import pytest

from toolbox import Style
from toolbox.utils import get_abs_path

from toolbox._logtool._logging import LogTool
from toolbox._logtool._utils import read_config, set_abs_path
from toolbox._logtool._formatter import ColorfulFormatter

##### FIXTURES #####

@pytest.fixture
def config_path():
    return 'tests/conf/logging_config.yml'

@pytest.fixture
def config_dict(config_path):
    return read_config(config_path)

@pytest.fixture
def logger_name():
    return __name__

@pytest.fixture
def logger_color():
    color = {'debug': Style.FG.BLUE,
             'info':'',
             'warning': Style.FG.YELLOW,
             'error': Style.FG.RED,
             'critical': Style(['BOLD'], 'RED'),
            }
    return color

##### TESTS #####

### _logtool/_logging.py ###
class TestLogTool:
    @staticmethod
    def test_set_logger(config_path, config_dict, logger_name):
        LogTool.set_logger(config_path)
        logger = logging.getLogger(logger_name)
        for handler in logger.handlers:
            assert handler.name in config_dict['handlers'].keys()
            assert handler.level == logging.getLevelName(config_dict['handlers'][handler.name]['level'])
    
    @staticmethod
    def test_get_logger(logger_name):
        assert LogTool.get_logger(logger_name) == logging.getLogger(logger_name)
    
    @staticmethod
    def test_colorful_logger(logger_name):
        LogTool.colorful_logger(logger_name)
        logger = logging.getLogger(logger_name)
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                assert isinstance(handler.formatter, ColorfulFormatter)

### _logtool/_utils.py ###
def test_read_config(config_path):
    config = read_config(config_path)
    assert isinstance(config, dict)

def test_set_abs_path(config_dict):
    expect_path = get_abs_path(config_dict['handlers']['errlog']['filename'])
    configured_dict = set_abs_path(config_dict, 'filename')
    assert configured_dict['handlers']['errlog']['filename'] == expect_path