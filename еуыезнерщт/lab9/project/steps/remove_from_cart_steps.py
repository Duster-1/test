from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

scenarios('../features/remove_from_cart.feature')


@given('the user is on the home page')
def user_on_home_page(driver):
    home_page = HomePage(driver)
    home_page.open()


@given('the user has added a product to the cart')
def user_added_product_to_cart(driver):
    home_page = HomePage(driver)
    home_page.search_product("Ноутбук")
    product_page = ProductPage(driver)
    product_page.add_to_cart()


@when('the user removes the product from the cart')
def user_removes_product_from_cart(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.remove_from_cart()


@then('the cart is empty')
def cart_is_empty(driver):
    cart_page = CartPage(driver)
    assert cart_page.is_cart_empty()
