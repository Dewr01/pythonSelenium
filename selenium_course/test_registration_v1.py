import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from web_init.web_driver import chrome_driver


def test_registration_form(link):
    browser = chrome_driver()
    browser.get(link)

    browser.find_element("css selector", ".first_block .first_class input.first").send_keys("Ivan")
    browser.find_element("css selector", ".first_block .second_class input.second").send_keys("Petrov")
    browser.find_element("css selector", ".first_block .third_class input.third").send_keys("test@test.com")
    browser.find_element("css selector", "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element("tag name", "h1").text
    return welcome_text


class TestForm(unittest.TestCase):
    def test_link1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            test_registration_form(link1),
            'Check all requiered fields'
        )

    def test_link2(self):
        link2 = 'https://suninjuly.github.io/registration2.html'
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            test_registration_form(link2),
            'Check all requiered fields'
        )


if __name__ == "__main__":
    unittest.main()
