import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")


driver.get('http://the-internet.herokuapp.com/checkboxes')

time.sleep(3)

print(driver.find_element(*CHECKBOX_1).is_selected())  # Получение статуса  с помощью метода is_selected()
#print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))  # Получение статуса по атрибуту "checked"
driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).is_selected())
#print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))

#driver.find_element(*CHECKBOX_1).is_selected()  # Проверяет доступен ли элемент для взаимодействия? True False

time.sleep(3)

# Если input checkbox перекрыт каким-то элементом, то мы сначала кликаем по элементу, а потом проверяем статус.