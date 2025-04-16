from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--window-size=1920,1080')
#options.add_argument('--headless')
options.add_argument("--user-agent=Automation")

driver = webdriver.Chrome(options=options)

CHECK_BOX_HOME_ACTION = ("xpath", "//span[@class='rct-checkbox']")
CHECK_BOX_HOME_STATUS = ("xpath", "//input[@type='checkbox']")

driver.get("https://demoqa.com/checkbox")

print(driver.find_element(*CHECK_BOX_HOME_STATUS).is_selected())

lable = driver.find_element(*CHECK_BOX_HOME_ACTION).click()

print(driver.find_element(*CHECK_BOX_HOME_STATUS).is_selected())
 
 


time.sleep(15)