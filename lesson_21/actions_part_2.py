import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # Импортируем ActionChains для работы с последовательностью действий


driver = webdriver.Chrome()               

action = ActionChains(driver)  # Создаем объект ActionChains




driver.get('https://demoqa.com/menu#')

MENU_ITEM_2_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
SUB_LIST_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")

menu_item_2 = driver.find_element(*MENU_ITEM_2_LOCATOR)
sub_list_menu = driver.find_element(*SUB_LIST_LOCATOR)

action.move_to_element(menu_item_2).pause(2).move_to_element(sub_list_menu).pause(2).perform()
time.sleep(3)


time.sleep(3) 