import time
from web_init.driver_manager import WebDriverManager

chrome_driver = WebDriverManager("chrome").get_driver()

try:
    # 1. Open vk.com
    chrome_driver.get("https://vk.com")
    time.sleep(2)  # Wait for page to load

    # 2. Get and print title
    vk_title = chrome_driver.title
    print(f"VK.com title: {vk_title}")

    # 3. Open ya.ru
    chrome_driver.get("https://ya.ru")
    time.sleep(2)  # Wait for page to load

    # 4. Get and print title
    ya_title = chrome_driver.title
    print(f"Ya.ru title: {ya_title}")

    # 5. Go back and assert we returned to vk.com
    chrome_driver.back()
    time.sleep(2)
    assert "vk.com" in chrome_driver.current_url.lower(), "Did not return to VK.com"
    print("Successfully returned to VK.com")

    # 6. Refresh the page
    chrome_driver.refresh()
    time.sleep(2)

    # 7. Get and print current URL
    current_url = chrome_driver.current_url
    print(f"Current URL after refresh: {current_url}")

    # 8. Go forward to ya.ru
    chrome_driver.forward()
    time.sleep(2)

    # 9. Verify URL changed to ya.ru
    assert "ya.ru" in chrome_driver.current_url.lower(), "Did not navigate to Ya.ru"
    print("Successfully navigated forward to Ya.ru")

finally:
    # Close the browser
    chrome_driver.quit()
