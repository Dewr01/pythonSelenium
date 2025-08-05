from web_init.chrome_driver import ChromeDriver
from web_init.firefox_driver import FirefoxDriver
from web_init.opera_driver import OperaDriver
from web_init.webkit_driver import WebKitDriver


class WebDriverManager:
    def __init__(self, browser="chrome", headless=False):
        self.browser = browser.lower()
        self.headless = headless

    def get_driver(self):
        if self.browser == "chrome":
            return ChromeDriver(self.headless).create_driver()
        elif self.browser == "firefox":
            return FirefoxDriver(self.headless).create_driver()
        elif self.browser == "opera":
            return OperaDriver(self.headless).create_driver()
        elif self.browser in ["webkit", "safari"]:
            return WebKitDriver(self.headless).create_driver()
        else:
            raise ValueError(
                f"Unsupported browser: {self.browser}. "
                "Supported browsers are 'chrome', 'firefox', 'opera', and 'webkit/safari'"
            )
