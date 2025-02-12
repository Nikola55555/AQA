import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/nl/login")
driver.find_element('id', 'loginformsubmit').click()  # Поиск элемента id со значением 'loginformsubmit', далее можно кликнуть на элемент, если нужно)