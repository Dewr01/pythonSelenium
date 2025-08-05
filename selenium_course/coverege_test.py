from web_init.web_driver import chrome_driver


browser = chrome_driver(headless=False)  # Set headless=True for headless mode

test_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

browser.get(test_url)

PAGE_SOURCE = browser.page_source
print(PAGE_SOURCE)
