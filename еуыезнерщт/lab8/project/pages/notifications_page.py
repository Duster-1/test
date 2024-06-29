from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NotificationsPage(BasePage):
    def go_to_notifications(self):
        self.wait_for_element(By.LINK_TEXT, "Особистий кабінет").click()
        self.wait_for_element(By.LINK_TEXT, "Сповіщення").click()

    def has_notifications(self):
        notifications = self.driver.find_elements(
            By.CSS_SELECTOR, ".notification__item")
        return len(notifications) > 0
