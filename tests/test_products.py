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
    
    def test_sort_products_a_to_z(self, page):
        """TC013: Sort products A to Z"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.sort_products("az")
        
        names = products_page.get_product_names()
        assert names == sorted(names), "Products not sorted A-Z"
        print("✅ TC013: Products sorted A-Z correctly")
    
    def test_sort_products_z_to_a(self, page):
        """TC014: Sort products Z to A"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.sort_products("za")
        
        names = products_page.get_product_names()
        assert names == sorted(names, reverse=True), "Products not sorted Z-A"
        print("✅ TC014: Products sorted Z-A correctly")
    
    def test_sort_products_price_low_to_high(self, page):
        """TC015: Sort products by price (low to high)"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.sort_products("lohi")
        
        prices = products_page.get_product_prices()
        assert prices == sorted(prices), "Products not sorted by price"
        print("✅ TC015: Products sorted by price correctly")
        