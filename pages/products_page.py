from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page Object for Products page"""
    
    # Selectors
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"
    INVENTORY_ITEM = ".inventory_item"
    
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
    
    def add_product_to_cart_by_name(self, product_name: str):
        """Add product to cart by name"""
        print(f"🔄 Agregando producto: {product_name}")
        button_selector = f"//div[@class='inventory_item'][.//div[text()='{product_name}']]//button"
        self.page.click(button_selector)
        print(f"✅ Producto '{product_name}' agregado")
    
    def get_cart_count(self) -> int:
        """Returns number of items in cart"""
        if self.is_visible(self.CART_BADGE):
            count_text = self.get_text(self.CART_BADGE)
            return int(count_text)
        return 0
    
    def get_cart_badge_count(self) -> str:
        """Returns cart badge text"""
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"
    
    def go_to_cart(self):
        """Navigate to cart"""
        print("🔄 Yendo al carrito...")
        self.click(self.CART_ICON)
        print("✅ En página del carrito")
    
    def is_product_button_remove(self, product_name: str) -> bool:
        """Verifies product button shows 'Remove'"""
        button_selector = f"//div[@class='inventory_item'][.//div[text()='{product_name}']]//button"
        button_text = self.page.text_content(button_selector)
        return "Remove" in button_text
    
    def sort_products(self, sort_option: str):
        """Sort products by selected option"""
        print(f"🔄 Ordenando productos: {sort_option}")
        sort_dropdown = self.page.locator(".product_sort_container")
        sort_dropdown.select_option(sort_option)
        print(f"✅ Productos ordenados: {sort_option}")
    
    def get_product_names(self) -> list:
        """Get list of all product names"""
        return self.page.locator(".inventory_item_name").all_text_contents()
    
    def get_product_prices(self) -> list:
        """Get list of all product prices as floats"""
        price_texts = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(price.replace("$", "")) for price in price_texts]
