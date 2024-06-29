from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RegistrationPage(BasePage):
    def register(self, email, password):
        self.wait_for_element(By.NAME, "register[login]").send_keys(email)
        self.wait_for_element(
            By.NAME, "register[password]").send_keys(password)
        self.wait_for_element(
            By.NAME, "register[password]").send_keys(Keys.RETURN)

    def is_registration_successful(self):
        success_message = self.wait_for_element(
            By.CLASS_NAME, "notification__content").text
        return "Вітаємо!" in success_message
