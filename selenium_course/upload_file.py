import os
import time
from web_init.web_driver import chrome_driver

browser = chrome_driver()
browser.get("https://suninjuly.github.io/file_input.html")

browser.find_element("name", "firstname").send_keys("Ivan")
browser.find_element("name", "lastname").send_keys("Petrov")
browser.find_element("name", "email").send_keys("test@test.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'upload_file.txt')
browser.find_element("name", "file").send_keys(file_path)

browser.find_element("css selector", "button.btn").click()
time.sleep(10)
