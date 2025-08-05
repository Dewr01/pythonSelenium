from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def chrome_driver(headless=False):
    try:
        options = ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")  # For Docker/limited resource environments
        options.add_argument("--no-sandbox")  # Bypass OS security model

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Failed to initialize Chrome driver: {str(e)}")
        raise


def firefox_driver(headless=False):
    try:
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
    except Exception as e:
        print(f"Failed to initialize Firefox driver: {str(e)}")
        raise
