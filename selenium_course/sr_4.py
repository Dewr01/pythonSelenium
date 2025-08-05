import math
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from web_init.web_driver import chrome_driver

browser = chrome_driver()

browser.get("https://suninjuly.github.io/explicit_wait2.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element("css selector", "button.btn").click()

browser.find_element("id", "answer").send_keys(
    calc(browser.find_element("id", "input_value").text)
)
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element("id", "solve").click()

time.sleep(10)
