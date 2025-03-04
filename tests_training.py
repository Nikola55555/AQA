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


SELECT_LOCATOR = ("xpath", "//input[@id='userName']")


driver.get('https://demoqa.com/text-box')

FULL_NAME = driver.find_element(*SELECT_LOCATOR)

FULL_NAME.send_keys('Николай')
time.sleep(3)