from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

scenarios('../features/registration.feature')


@given('the user is on the registration page')
def user_on_registration_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_registration()


@when('the user registers with email "test@example.com" and password "Password123"')
def user_registers(driver):
    registration_page = RegistrationPage(driver)
    registration_page.register("test@example.com", "Password123")


@then('the user sees a registration success message')
def registration_success_message(driver):
    registration_page = RegistrationPage(driver)
    assert registration_page.is_registration_successful()
