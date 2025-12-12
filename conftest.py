import pytest
from pathlib import Path
from datetime import datetime
from core.browser_manager import BrowserManager


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar el resultado del test"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function")
def page(request):
    """Fixture que proporciona una página de Playwright"""
    browser_manager = BrowserManager()
    page = browser_manager.get_page()
    
    yield page
    
    # Screenshot on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = screenshot_dir / f"{test_name}_{timestamp}.png"
        
        page.screenshot(path=str(screenshot_path))
        print(f"\n📸 Screenshot guardado: {screenshot_path}")
    
    browser_manager.close()
    