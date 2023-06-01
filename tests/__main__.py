import pytest

class MyPlugin:
    def pytest_sessionstart(self):
        pass
    def pytest_sessionfinish(self):
        pass


if __name__ == "__main__":
    pytest.main(['--cache-clear', '--verbose', '--show-capture=stdout'], plugins=[])