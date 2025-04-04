from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--window-size=1920,1080')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

FULL_NAME_LOCATOR = ("xpath", "//input[@id='userName']")
EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
Current_Address = ("xpath", "//textarea[@id='currentAddress']")

driver.get('https://demoqa.com/text-box')

driver.find_element('xpath', '//input[@placeholder="Full Name"]').send_keys('Николай')
driver.find_element(*EMAIL_FIELD).send_keys('bagbee84@mail.ru')
driver.find_element(*Current_Address).send_keys("Привет! Как дела?")


time.sleep(3)