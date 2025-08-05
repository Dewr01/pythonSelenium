from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    def __init__(self, headless=False):
        self.headless = headless

    def create_driver(self):
        try:
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")

            if self.headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")

            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"Failed to initialize Chrome driver: {str(e)}")
            raise
        