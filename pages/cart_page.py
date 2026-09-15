import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CART_BADGE = ".shopping_cart_badge"

    def get_cart_items_count(self) -> int:
        items = self.page.locator(self.CART_ITEMS)
        items.first.wait_for(state="visible", timeout=5000)
        return items.count()

    def get_cart_item_names(self) -> list[str]:
        return self.page.locator(self.CART_ITEM_NAME).all_inner_texts()

    def go_to_checkout(self) -> None:
        self.page.locator(self.CHECKOUT_BUTTON).click()

    def continue_shopping(self) -> None:
        self.page.locator(self.CONTINUE_SHOPPING_BUTTON).click()

    def remove_product(self, product_name: str) -> None:
        exact_name = re.compile(rf"^{re.escape(product_name)}$")

        product = self.page.locator(self.CART_ITEMS).filter(
            has=self.page.locator(
                self.CART_ITEM_NAME,
                has_text=exact_name,
            )
        )

        expect(
            product,
            message=f"El producto {product_name!r} no está en el carrito",
        ).to_have_count(1)

        product.get_by_role("button", name="Remove").click()

