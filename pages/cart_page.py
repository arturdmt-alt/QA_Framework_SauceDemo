from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CART_BADGE = ".shopping_cart_badge"

    def get_cart_items_count(self):
        items = self.page.locator(self.CART_ITEMS).all()
        count = len(items)
        print(f"📦 Products in cart: {count}")
        return count

    def get_cart_item_names(self):
        items = self.page.locator(self.CART_ITEM_NAME).all()
        return [item.text_content() for item in items]

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def remove_product(self, product_name):
        print(f"🗑️ Removing product: {product_name}")

        button = self.page.locator(
            f"//div[contains(@class,'cart_item')]"
            f"[.//div[@class='inventory_item_name' and text()='{product_name}']]"
            f"//button"
        )

        button.wait_for(state="visible", timeout=5000)
        button.click()

        print(f"✅ Product '{product_name}' removed")
