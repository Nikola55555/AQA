import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#service = Service(executable_path=ChromeDriverManager().install())
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://demoqa.com/alerts')

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()   # Ждем пока элемент станет кликабельным и кликаем на него

alert = wait.until(EC.alert_is_present())   # Ждем появления alert

driver.switch_to.alert  # Переключаемся на  alert

time.sleep(3)

alert.accept()   # Принимаем  alert

time.sleep(3)
#
