from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_cart(self):
        self.wait_for_element(By.CSS_SELECTOR, ".buy-button__label").click()
