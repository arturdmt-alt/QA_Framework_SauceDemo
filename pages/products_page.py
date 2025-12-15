def add_product(self, product_name):
    product_id = product_name.lower().replace(" ", "-")
    add_button = f"#add-to-cart-{product_id}"

    if self.page.locator(add_button).count() > 0:
        self.page.click(add_button)

