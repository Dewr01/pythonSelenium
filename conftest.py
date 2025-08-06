import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    print("\nquit browser..")
    browser.quit()
