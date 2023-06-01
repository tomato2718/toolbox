import pytest

from toolbox import LogTool

from toolbox._handle._exception_handler import Handle

LogTool.set_logger('tests/conf/logging_config.yml')
logger = LogTool.get_logger('__main__')

##### FIXTURES #####

##### TESTS #####

### _handle/_exception_handler.py ###

class TestHandle:
    
    @staticmethod
    def test_Raise():
        @Handle.Raise()
        def woops():
            raise Exception('woops')

        with pytest.raises(Exception):
            woops()
    
    @staticmethod
    def test_Ignore():
        @Handle.Ignore()
        def woops():
            raise Exception('woops')

        woops()

    @staticmethod
    def test_Return():
        @Handle.Return(return_= 'foo')
        def woops():
            raise Exception('woops')

        assert woops() == 'foo'

    @staticmethod
    def test_Log(caplog):
        @Handle.Log(logger='__main__')
        def woops():
            raise Exception('woops')

        woops()
        assert any('woops' in record.msg for record in caplog.records)