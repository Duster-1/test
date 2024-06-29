import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.notifications_page import NotificationsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    yield driver
    driver.quit()


def test_user_notifications(driver):
    home_page = HomePage(driver)
    notifications_page = NotificationsPage(driver)

    home_page.open()
    home_page.go_to_registration()
    registration_page.register("test@example.com", "Password123")
    notifications_page.go_to_notifications()

    assert notifications_page.has_notifications()
