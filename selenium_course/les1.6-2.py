import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())

browser = webdriver.ChromeOptions()
browser.add_argument('--no-sandbox')
browser = webdriver.Chrome(service=service, options=browser)

time.sleep(5)

browser.get("http://suninjuly.github.io/find_xpath_form")

# Заполняем форму
input1 = browser.find_element(By.NAME, "first_name")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")

# Отправляем заполненную форму
button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button.click()

time.sleep(10)
