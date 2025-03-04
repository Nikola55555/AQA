import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # Импортируем ActionChains для работы с последовательностью действий
from scrolls import Scrolls

driver = webdriver.Chrome()               
action = ActionChains(driver)  # Создаем объект ActionChains
scroll = Scrolls(driver, action)

driver.get('https://seiyria.com/bootstrap-slider/')

EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
EX_2 = driver.find_element(*EX_2_LOCATOR)

scroll.scroll_to_element(EX_2)  # Используем методы из класса Scrolls

time.sleep(5)