import pytest
from core.browser_manager import BrowserManager

@pytest.fixture(scope="session")
def browser_manager():
    manager = BrowserManager()
    yield manager
    manager.close()

@pytest.fixture(scope="function")
def page(browser_manager):
    return browser_manager.start()
