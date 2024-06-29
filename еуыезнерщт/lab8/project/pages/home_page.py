from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://rozetka.com.ua/"

    def open(self):
        self.driver.get(self.url)

    def go_to_registration(self):
        self.wait_for_element(By.LINK_TEXT, "Входити").click()
        self.wait_for_element(By.LINK_TEXT, "Зареєструватися").click()

    def search_product(self, product_name):
        search_box = self.wait_for_element(By.NAME, "search")
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
