import pytest

from toolbox.utils import get_abs_path

from toolbox.metaclasses._meta import PathMeta

##### FIXTURES #####

##### TESTS #####

### metaclasses/_meta.py ###
def test_PathMeta():
    class Path(metaclass=PathMeta):
        FOO = 'foo'
        BAR = 'b/a/r'

    assert Path.FOO == get_abs_path('foo')
    assert Path.BAR == get_abs_path('b/a/r')
