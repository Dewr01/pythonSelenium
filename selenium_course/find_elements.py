from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

icon = driver.find_element("class name", "wikipedia-search-wiki-link")
print(icon)

search_field = driver.find_element("id", "name")
print(search_field)

search_button = driver.find_element("class name", "wikipedia-search-button")
print(search_button)

tag_name = driver.find_elements("tag name", "button")
print(tag_name)
