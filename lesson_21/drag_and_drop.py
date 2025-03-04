import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # Импортируем ActionChains для работы с последовательностью действий


driver = webdriver.Chrome()               

action = ActionChains(driver)  # Создаем объект ActionChains

driver.get('https://the-internet.herokuapp.com/drag_and_drop')

COLUMN_A = ("xpath", "//div[@id='column-a']")
COLUMN_B = ("xpath", "//div[@id='column-b']")

A = driver.find_element(*COLUMN_A)
B = driver.find_element(*COLUMN_B)

time.sleep(3)
action.drag_and_drop(A, B).perform()   #Для перемещения элемента, указываем что и куда перетаскиваем
time.sleep(3)

