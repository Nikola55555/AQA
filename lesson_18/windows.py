import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--windows-size=1920,1080')
driver = webdriver.Chrome(options=options)
 # locators

FOR_BUSINESS_BUTTONLOCATOR = ("xpath", "//a[text() = 'For Business']")
START_FOR_FREE = ("xpath", "//div[@class='text-block-3']")

driver.get("https://hyperskill.org/")

time.sleep(5)
driver.find_element(*FOR_BUSINESS_BUTTONLOCATOR).click()

time.sleep(3)

driver.find_element(*START_FOR_FREE).click()

time.sleep(3)

tabs = driver.window_handles  # Записываем в переменную дескрипторы всех окон и вкладок открытых

driver._switch_to.window(tabs[1]) # Выбрали нужную вклдаку

time.sleep(3)

email = driver.find_element("xpath", "//input[@id='__BVID__173']").click()
email.send_keys("JJJJJJJJJ@jJJJJJ")

time.sleep(3)

# window = driver.switch_to.new_window('tab')   # Можно так переключиться на новую вкладку (указываем tab или окно window)