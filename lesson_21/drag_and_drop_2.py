import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # Импортируем ActionChains для работы с последовательностью действий


driver = webdriver.Chrome()               

action = ActionChains(driver)  # Создаем объект ActionChains

driver.get('https://tympanus.net/Development/DragDropInteractions/sidebar.html')

GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[2]")


time.sleep(1)
action.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()  

time.sleep(3)

#    click_and_hold  - нажимаем и удерживаем элемент
#    move_to_elemen  - перемещаемся к элементу
#    release         - отпускаем кнопку мыши
     


