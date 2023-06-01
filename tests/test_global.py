import pytest

from toolbox._global import Global

##### FIXTURES #####

##### TESTS #####

### _global.py ###
def test_Global():
    bar = 'bar'
    Global.foo = bar
    assert Global.foo == bar