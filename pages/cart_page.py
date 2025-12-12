from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for Cart page"""
    
    # Selectors
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    REMOVE_BUTTON = "button[id^='remove']"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING = "#continue-shopping"
    
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/cart.html"
    
    def get_cart_items_count(self) -> int:
        """Returns number of items in cart"""
        items = self.page.locator(self.CART_ITEM).count()
        print(f"📦 Productos en carrito: {items}")
        return items
    
    def get_product_names(self) -> list:
        """Returns list of product names in cart"""
        names = self.page.locator(self.ITEM_NAME).all_text_contents()
        print(f"📋 Productos: {names}")
        return names
    
    def get_product_price(self, product_name: str) -> str:
        """Returns price for specific product"""
        price_selector = f"//div[@class='cart_item'][.//div[text()='{product_name}']]//div[@class='inventory_item_price']"
        price = self.page.text_content(price_selector)
        print(f"💰 Precio de '{product_name}': {price}")
        return price
    
    def remove_product(self, product_name: str):
        """Removes product from cart"""
        print(f"🗑️ Removiendo producto: {product_name}")
        button_selector = f"//div[@class='cart_item'][.//div[text()='{product_name}']]//button"
        self.click(button_selector)
        print(f"✅ Producto '{product_name}' removido")
    
    def go_to_checkout(self):
        """Navigate to checkout"""
        print("🔄 Iniciando checkout...")
        self.click(self.CHECKOUT_BUTTON)
        print("✅ En página de checkout")
    
    def continue_shopping(self):
        """Return to products page"""
        print("🔄 Volviendo a productos...")
        self.click(self.CONTINUE_SHOPPING)
        print("✅ De vuelta en productos")
        
        