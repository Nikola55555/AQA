import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--windows-size=1920,1080')
driver = webdriver.Chrome(options=options)               

FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='name']")

driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(3)
driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys('Николай')
time.sleep(3)

# переключаемся на iframe и работаем в нем
driver.switch_to.frame('iframe1')

# Находясь внутри iframе можем переключаться на детей 
driver.switch_to.frame(0)  # здесь мы указали индекс фрейма 

# для перехода к родительскому iframe 

driver.switch_to.parent_frame()
