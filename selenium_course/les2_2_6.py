import math
import time
from selenium.webdriver.support.select import Select
from web_init.web_driver import chrome_driver

browser = chrome_driver()
browser.get("https://suninjuly.github.io/execute_script.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element("id", "answer").send_keys(
    calc(browser.find_element("id", "input_value").text)
)

browser.find_element("id", "robotCheckbox").click()

browser.execute_script("document.querySelector('footer').remove()")

browser.find_element("id", "robotsRule").click()

browser.find_element("tag name", "button").click()

time.sleep(10)
