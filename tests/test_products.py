import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
class TestProducts:
    """Tests for Products functionality"""
    
    def test_add_single_product(self, page):
        """TC002: Add single product to cart"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        
        # Validate cart badge shows "1"
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "1"
        print("✅ TC002: Producto agregado al carrito")
    
    @pytest.mark.smoke
    def test_add_multiple_products(self, page):
        """TC003: Add multiple products to cart"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        products_page.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        
        # Validate badge shows "3"
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "3"
        print("✅ TC003: Múltiples productos agregados")
        