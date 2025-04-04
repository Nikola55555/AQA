import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import  Select

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


SELECT_LOCATOR = ("xpath", "//button[text()='Add Element']")


driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
time.sleep(3)
add_element = driver.find_element(*SELECT_LOCATOR).click()
time.sleep(3)
add_element2 = driver.find_element(*SELECT_LOCATOR).click()
time.sleep(3)
add_element3 = driver.find_element(*SELECT_LOCATOR).click()
time.sleep(3)