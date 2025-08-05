import time
from selenium.webdriver.support.select import Select
from web_init.web_driver import chrome_driver

browser = chrome_driver()
browser.get("https://suninjuly.github.io/selects1.html")

select = Select(browser.find_element("tag name", "select"))
select.select_by_value(
    str(int(browser.find_element("id", "num1").text) + int(browser.find_element("id", "num2").text))
)

browser.find_element("css selector", "button.btn").click()

time.sleep(10)
