import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage


@pytest.mark.e2e
@pytest.mark.smoke
class TestE2E:
    """End-to-End Tests - Complete flows"""
    
    def test_complete_purchase_flow(self, page):
        """TC011: Complete purchase flow from login to confirmation"""
        # Login
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Add products
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        
        # Go to cart
        products_page.go_to_cart()
        cart_page = CartPage(page)
        assert cart_page.get_cart_items_count() == 2
        
        # Checkout
        cart_page.go_to_checkout()
        checkout_page = CheckoutPage(page)
        checkout_page.fill_information("Juan", "Perez", "1234")
        checkout_page.click_continue()
        checkout_page.click_finish()
        
        # Validate confirmation
        confirmation_page = ConfirmationPage(page)
        assert confirmation_page.is_order_complete()
        print("✅ TC011: Flujo E2E completo exitoso")
        
        