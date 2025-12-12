import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
class TestLogin:
    """Tests for Login functionality"""
    
    def test_login_success(self, page):
        """TC001: Successful login with valid credentials"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Validate we're on products page
        assert "/inventory.html" in page.url
        print("✅ TC001: Login exitoso")
        