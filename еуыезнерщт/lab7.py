from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path='/path/to/chromedriver')


base_url = "https://rozetka.com.ua/"


def test_user_registration():
    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Входити").click()
    driver.find_element(By.LINK_TEXT, "Зареєструватися").click()

    driver.find_element(By.NAME, "register[login]").send_keys(
        "test@example.com")
    driver.find_element(By.NAME, "register[password]").send_keys("Password123")
    driver.find_element(By.NAME, "register[password]").send_keys(Keys.RETURN)

    time.sleep(5)

    success_message = driver.find_element(
        By.CLASS_NAME, "notification__content").text
    assert "Вітаємо!" in success_message

    driver.quit()


test_user_registration()


def test_add_product_to_cart():
    driver.get(base_url)

    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Ноутбук")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".goods-tile__heading a").click()

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".buy-button__label").click()

    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Кошик").click()

    time.sleep(3)
    cart_item = driver.find_element(
        By.CSS_SELECTOR, ".cart-product__title").text
    assert "Ноутбук" in cart_item

    driver.quit()


test_add_product_to_cart()


def test_remove_product_from_cart():
    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Кошик").click()

    time.sleep(3)
    driver.find_element(
        By.CSS_SELECTOR, ".cart-product__button-remove").click()

    time.sleep(3)
    empty_cart_message = driver.find_element(By.CLASS_NAME, "cart-dummy").text
    assert "Кошик порожній" in empty_cart_message

    driver.quit()


test_remove_product_from_cart()


def test_user_notifications():
    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Входити").click()
    driver.find_element(By.NAME, "login").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Особистий кабінет").click()

    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Сповіщення").click()

    time.sleep(3)
    notifications = driver.find_elements(
        By.CSS_SELECTOR, ".notification__item")
    assert len(notifications) > 0

    driver.quit()


test_user_notifications()
