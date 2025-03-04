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

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")


driver.get('https://demoqa.com/select-menu')

driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")           #  Чтобы выбрался необходимый элемент, надо нажать Enter
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)