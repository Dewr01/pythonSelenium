from selenium import webdriver
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.safari.service import Service as SafariService


class WebKitDriver:
    def __init__(self, headless=False):
        self.headless = headless

    def create_driver(self):
        try:
            if self.headless:
                print("Warning: Safari/WebKit doesn't support headless mode on all platforms")

            options = SafariOptions()
            service = SafariService()
            return webdriver.Safari(service=service, options=options)
        except Exception as e:
            print(f"Failed to initialize WebKit/Safari driver: {str(e)}")
            raise
