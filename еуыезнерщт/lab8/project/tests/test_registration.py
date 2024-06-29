import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    yield driver
    driver.quit()


def test_user_registration(driver):
    home_page = HomePage(driver)
    registration_page = RegistrationPage(driver)

    home_page.open()
    home_page.go_to_registration()
    registration_page.register("test@example.com", "Password123")

    assert registration_page.is_registration_successful()
