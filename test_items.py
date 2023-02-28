from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(30)
    add_to_cart_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_cart_button is not None, "'Add to cart button' not found!"