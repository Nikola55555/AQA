import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import  Select


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")


driver.get('http://the-internet.herokuapp.com/dropdown')

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
time.sleep(3)
#DROPDOWN.select_by_value("2")  # Ещё вариант выбора, по 'value'
DROPDOWN.select_by_index(1)

time.sleep(2)