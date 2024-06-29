import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    yield driver
    driver.quit()


def test_remove_product_from_cart(driver):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    home_page.open()
    home_page.search_product("Ноутбук")
    product_page.add_to_cart()
    cart_page.open_cart()
    cart_page.remove_from_cart()

    assert cart_page.is_cart_empty()
