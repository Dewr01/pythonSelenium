import math
import time
from web_init.web_driver import chrome_driver

browser = chrome_driver()
browser.get("https://suninjuly.github.io/redirect_accept.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element("css selector", "button.btn").click()

browser.switch_to.window(browser.window_handles[1])

browser.find_element("id", "answer").send_keys(
    calc(browser.find_element("id", "input_value").text)
)

browser.find_element("css selector", "button.btn").click()

time.sleep(10)