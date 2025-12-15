from pages.base_page import BasePage


class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON_TEMPLATE = (
        "//div[@class='inventory_item']"
        "[.//div[text()='{}']]//button"
    )
    CART_BADGE = ".shopping_cart_badge"

    def add_product_to_cart(self, product_name):
        print(f"➕ Adding product: {product_name}")

        button = self.page.locator(
            self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_name)
        )

        button.wait_for(state="visible", timeout=5000)
        button.click()

        print(f"✅ Product '{product_name}' added")

    def get_cart_badge_count(self):
        badge = self.page.locator(self.CART_BADGE)

        if badge.is_visible():
            count = badge.text_content()
        else:
            count = "0"

        print(f"🛒 Cart badge count: {count}")
        return count

