from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object for Checkout (information and overview)"""
    
    # Selectors - Step One (Information)
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"
    
    # Selectors - Step Two (Overview)
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"
    FINISH_BUTTON = "#finish"
    
    def __init__(self, page):
        super().__init__(page)
    
    def fill_information(self, first_name: str, last_name: str, zip_code: str):
        """Fill checkout information form"""
        print(f"📝 Llenando información: {first_name} {last_name}")
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.ZIP_CODE, zip_code)
        print("✅ Información completada")
    
    def click_continue(self):
        """Navigate to overview page"""
        print("🔄 Continuando a overview...")
        self.click(self.CONTINUE_BUTTON)
        print("✅ En checkout overview")
    
    def get_error_message(self) -> str:
        """Returns error message if present"""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def get_item_total(self) -> str:
        """Returns item subtotal"""
        text = self.get_text(self.ITEM_TOTAL)
        