import math
import time
from web_init.web_driver import chrome_driver

browser = chrome_driver()
browser.get("https://suninjuly.github.io/math.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element("id", "input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element("id", "answer")
answer_input.send_keys(y)

robot_check = browser.find_element("id", "robotCheckbox")
robot_check.click()

robots_rule = browser.find_element("id", "robotsRule")
robots_rule.click()

button_click = browser.find_element("css selector", "button.btn")
button_click.click()

time.sleep(10)
