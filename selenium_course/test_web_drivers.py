from web_init.driver_manager import WebDriverManager

line = "https://ya.ru"

chrome_driver = WebDriverManager("chrome").get_driver()
chrome_driver.get(line)
print(f"{line}: ", chrome_driver.title)
chrome_driver.quit()
