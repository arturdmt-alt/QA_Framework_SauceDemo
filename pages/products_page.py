from pages.base_page import BasePage


class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON_TEMPLATE = (
        "//div[contains(@class,'inventory_item')]"
        "[.//div[text()='{}']]//button"
    )
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def add_product_to_cart_by_name(self, product_name):
        button = self.page.locator(
            self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_name)
        )
        button.wait_for(state="visible", timeout=5000)
        button.click()

    # compatibilidad
    def add_product_to_cart(self, product_name):
        self.add_product_to_cart_by_name(product_name)

    def get_cart_badge_count(self):
        badge = self.page.locator(self.CART_BADGE)
        return badge.text_content() if badge.is_visible() else "0"

    def go_to_cart(self):
        cart = self.page.locator(self.CART_LINK)
        cart.wait_for(state="visible", timeout=5000)
        cart.click()
    SORT_DROPDOWN = ".product_sort_container"

    def sort_products(self, sort_order):
        """Sort products: az, za, lohi, hilo"""
        dropdown = self.page.locator(self.SORT_DROPDOWN)
        dropdown.select_option(sort_order)

