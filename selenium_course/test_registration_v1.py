import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestRegistration(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)

    def tearDown(self):
        self.browser.quit()

    def fill_form(self, browser):
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input.third").send_keys("test@test.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        welcome_text = self.fill_form(self.browser)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        welcome_text = self.fill_form(self.browser)
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)


if __name__ == "__main__":
    unittest.main()
