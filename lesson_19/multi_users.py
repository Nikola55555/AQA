import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--windows-size=1920,1080')
user1 = webdriver.Chrome(options=options)               # Для реализации возможности регистрации нескольких пользователей, присваиваем переменной webdriver

LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

user1.get("https://hyperskill.org/login")

user1.find_element(*LOGIN_FIELD).send_keys("ghost@ya.ru")
user1.find_element(*PASSWORD_FIELD).send_keys("1112233")
user1.find_element(*SUBMIT_BUTTON).click()

time.sleep(5)

user2 = webdriver.Chrome(options=options) 
user2.get("https://hyperskill.org/login")

user2.find_element(*LOGIN_FIELD).send_keys("bagbee84@ya.ru")
user2.find_element(*PASSWORD_FIELD).send_keys("555888222")
user2.find_element(*SUBMIT_BUTTON).click()

# Далее уже работаем с двумя разными окнами и разными объектами webdriver