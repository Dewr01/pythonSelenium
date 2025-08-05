from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OperaOptions
from selenium.webdriver.chrome.service import Service as OperaService
from webdriver_manager.opera import OperaDriverManager


class OperaDriver:
    def __init__(self, headless=False):
        self.headless = headless

    def create_driver(self):
        try:
            options = OperaOptions()

            if self.headless:
                options.add_argument('--headless')
                options.add_argument('--window-size=1920,1080')

            options.add_argument('--start-maximized')
            service = OperaService(OperaDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"Failed to initialize Opera driver: {str(e)}")
            raise
