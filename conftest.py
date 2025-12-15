import pytest
from core.browser_manager import BrowserManager

@pytest.fixture(scope="session")
def browser_manager():
    manager = BrowserManager()
    yield manager
    manager.close()

@pytest.fixture(scope="function")
def page(browser_manager):
    page = browser_manager.start()
    yield page
    page._context.close()

