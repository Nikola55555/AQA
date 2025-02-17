import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



chrome_options = webdriver.ChromeOptions()

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')


time.sleep(3)

# Находим элемент input по хpath  и посылаем путь до нашего файла.
driver.find_element("xpath", "//input[@type= 'file']").send_keys(f'{os.getcwd()}/Downloads/ObjectivityTestAutomationCSHarpFramework.txt')


time.sleep(3)


# Если функция загрузки файла реализованна с помощью кнопки и не видно inputa, то ищем его всеравно через хpath и вставляем путь.