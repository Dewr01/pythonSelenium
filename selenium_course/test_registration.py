from selenium.common.exceptions import NoSuchElementException
from web_init.web_driver import chrome_driver


def test_registration_form(link):
    browser = chrome_driver()
    browser.get(link)

    browser.find_element("css selector", ".first_block .first_class input.first").send_keys("Ivan")

    browser.find_element("css selector", ".first_block .second_class input.second").send_keys("Petrov")

    browser.find_element("css selector", ".first_block .third_class input.third").send_keys("test@test.com")

    browser.find_element("css selector", "button.btn").click()

    welcome_text = browser.find_element("tag name", "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text


# Тест должен пройти на первой странице
test_registration_form("http://suninjuly.github.io/registration1.html")

# Тест должен упасть на второй странице
try:
    test_registration_form("http://suninjuly.github.io/registration2.html")
except NoSuchElementException:
    print("Тест на второй странице упал с NoSuchElementException как и ожидалось")
