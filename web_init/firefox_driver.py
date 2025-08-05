from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxDriver:
    def __init__(self, headless=False):
        self.headless = headless

    def create_driver(self):
        try:
            options = FirefoxOptions()

            if self.headless:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")

            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)
        except Exception as e:
            print(f"Failed to initialize Firefox driver: {str(e)}")
            raise
        