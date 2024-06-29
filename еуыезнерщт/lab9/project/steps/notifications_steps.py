from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.notifications_page import NotificationsPage
from pages.registration_page import RegistrationPage

scenarios('../features/notifications.feature')


@given('the user is logged in')
def user_logged_in(driver):
    home_page = HomePage(driver)
    registration_page = RegistrationPage(driver)
    home_page.open()
    home_page.go_to_registration()
    registration_page.register("test@example.com", "Password123")


@when('the user navigates to the notifications page')
def user_navigates_to_notifications(driver):
    notifications_page = NotificationsPage(driver)
    notifications_page.go_to_notifications()


@then('the user sees notifications')
def user_sees_notifications(driver):
    notifications_page = NotificationsPage(driver)
    assert notifications_page.has_notifications()
