import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # Импортируем ActionChains для работы с последовательностью действий


driver = webdriver.Chrome()               

action = ActionChains(driver)  # Создаем объект ActionChains


LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClick']")
HOVER_BUTTON_LOCATOR = ("xpath", "//button[@id='colorChangeOnHover']")

driver.get('https://testkru.com/Elements/Buttons')

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)

time.sleep(3)

# action.click(left_button).perform()  # perform() - замыкает цепочку действий

#action.click(left_button).perform()   # Сделали  клик по элементу левой кнопкой мыши
#action.double_click(double_button).perform() # Сделали двойной клик по элементу
#action.context_click(right_button).perform() # Сделали правый клик по элементу
#action.click(left_button).double_click(double_button).context_click(right_button).perform()  # Создали цепочку действий
#action.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button).pause(2).perform()  # Создали цепочку действий
  # c паузами между действиями

action.move_to_element(hover_button).perform()  # Наводим мышь на элемет



time.sleep(3) 