import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru")

login_button = driver.find_element('xpath', '//a[@id="login-desktop"]') # Находим элемент 'Войти'
login_button.click()

email_field = driver.find_element('xpath', '//input[@id = "login_email"]')  # Находим поле ввода email
email_field.send_keys("bagbee84@mail.ru")  # Вводим в поле почтовый адрес

print(email_field.get_attribute('value'))  # Выводим на печать записаное значение в поле "login_email"
time.sleep(3)

email_field.clear()  # Очищаем поле "login_email"
email_field.send_keys("<EMAIL>") # Вводим новое значение в поле "login_email"
time.sleep(3)