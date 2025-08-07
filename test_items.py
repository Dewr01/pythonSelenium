import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(10)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Add to basket button is not found"
