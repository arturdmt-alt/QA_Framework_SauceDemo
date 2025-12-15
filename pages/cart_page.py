from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    REMOVE_BUTTON_TEMPLATE = "//div[@class='cart_item'][.//div[text()='{}']]//button"
    CART_BADGE = ".shopping_cart_badge"

    def get_cart_items_count(self):
        """Returns number of items in cart"""
        items = self.page.locator(self.CART_ITEMS).all()
        count = len(items)
        print(f"📦 Products in cart: {count}")
        return count

    def get_cart_item_names(self):
        """Returns list of product names in cart"""
        items = self.page.locator(self.CART_ITEM_NAME).all()
        return [item.text_content() for item in items]

    def click_checkout(self):
        """Click Checkout button"""
        print("🔄 Starting checkout...")
        self.click(self.CHECKOUT_BUTTON)
        print("✅ On checkout page")

    def click_continue_shopping(self):
        """Click Continue Shopping"""
        print("🔄 Going back to products...")
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        print("✅ Back on products")

    def remove_product(self, product_name):
        """Remove product from cart by name"""
        print(f"🗑️ Removing product: {product_name}")
        button_selector = self.REMOVE_BUTTON_TEMPLATE.format(product_name)
        self.click(button_selector)
        print(f"✅ Product '{product_name}' removed")
        