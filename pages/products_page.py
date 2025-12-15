from pages.base_page import BasePage


class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON_TEMPLATE = (
        "//div[contains(@class,'inventory_item')]"
        "[.//div[text()='{}']]//button"
    )
    CART_BADGE = ".shopping_cart_badge"

    def add_product_to_cart_by_name(self, product_name):
        button = self.page.locator(
            self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_name)
        )
        button.wait_for(state="visible", timeout=5000)
        button.click()

    # alias por compatibilidad (por si algún test viejo lo usa)
    def add_product_to_cart(self, product_name):
        self.add_product_to_cart_by_name(product_name)

    def get_cart_badge_count(self):
        badge = self.page.locator(self.CART_BADGE)
        return badge.text_content() if badge.is_visible() else "0"

