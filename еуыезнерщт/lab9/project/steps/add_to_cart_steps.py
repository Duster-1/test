from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

scenarios('../features/add_to_cart.feature')


@given('the user is on the home page')
def user_on_home_page(driver):
    home_page = HomePage(driver)
    home_page.open()


@when('the user searches for "Ноутбук"')
def user_searches_product(driver):
    home_page = HomePage(driver)
    home_page.search_product("Ноутбук")


@when('the user adds the first product to the cart')
def user_adds_product_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.add_to_cart()


@then('the product "Ноутбук" is in the cart')
def product_in_cart(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()
    assert cart_page.is_product_in_cart("Ноутбук")
