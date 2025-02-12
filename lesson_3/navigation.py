import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://google.ru")

time.sleep(5) # Задержка 5 сек.

driver.back() # Перейти назад
time.sleep(3)

driver.forward() # Перейти вперед
time.sleep(3)

driver.refresh() # Обновить страницу
time.sleep(3)