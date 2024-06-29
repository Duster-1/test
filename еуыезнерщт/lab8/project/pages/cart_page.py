from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def open_cart(self):
        self.wait_for_element(By.LINK_TEXT, "Кошик").click()

    def remove_from_cart(self):
        self.wait_for_element(
            By.CSS_SELECTOR, ".cart-product__button-remove").click()

    def is_cart_empty(self):
        empty_cart_message = self.wait_for_element(
            By.CLASS_NAME, "cart-dummy").text
        return "Кошик порожній" in empty_cart_message

    def is_product_in_cart(self, product_name):
        cart_items = self.driver.find_elements(
            By.CSS_SELECTOR, ".cart-product__title")
        for item in cart_items:
            if product_name in item.text:
                return True
        return False
