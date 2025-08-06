import math
import time
from web_init.web_driver import chrome_driver

browser = chrome_driver()
browser.get(" http://suninjuly.github.io/get_attribute.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element("id", "answer").send_keys(
    calc(browser.find_element("id", "treasure").get_attribute("valuex"))
)

browser.find_element("id", "robotCheckbox").click()
browser.find_element("id", "robotsRule").click()
browser.find_element("css selector", "button.btn").click()

time.sleep(10)
