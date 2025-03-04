import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import  Select
from selenium.webdriver import Keys                                    # Импортируем Keys для работы с клавиатурой

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

KEYBOARD_INPUT = ("xpath", "//input[@id='target']")


driver.get('http://the-internet.herokuapp.com/key_presses')

#driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.ENTER)   # Вводим Enter
driver.find_element(*KEYBOARD_INPUT).send_keys('asdfghjkkmnbv')
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + "A")  # Вводим комбинацию клавиш Ctrl + A

time.sleep(2)