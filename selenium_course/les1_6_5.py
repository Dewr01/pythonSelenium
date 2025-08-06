import time
from selenium.webdriver.common.by import By

from web_init.web_driver import chrome_driver

link = "https://suninjuly.github.io/registration1.html"
link2= "https://suninjuly.github.io/registration2.html"

try:
    browser = chrome_driver()
    time.sleep(5)
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "[required]")
    for element in elements:
        element.send_keys("Ответ")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(15)
    browser.quit()
