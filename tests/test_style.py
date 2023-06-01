import pytest

from toolbox import Style

##### FIXTURES #####
@pytest.fixture
def font_bold():
    return '\033[1m'

@pytest.fixture
def fg_red():
    return '\033[31m'

@pytest.fixture
def bg_blue():
    return '\033[44m'

@pytest.fixture
def complex_style():
    return '\033[1;31;44m'

##### TESTS #####

### file.py ###
class TestStyle:
    @staticmethod
    def test_Font(font_bold):
        assert Style.Font.BOLD == font_bold

    @staticmethod
    def test_FG(fg_red):
        assert Style.FG.RED == fg_red
    
    @staticmethod
    def test_BG(bg_blue):
        assert Style.BG.BLUE == bg_blue

    @staticmethod
    def test_Style(complex_style):
        assert Style(['BOLD'], 'RED', 'BLUE') == complex_style