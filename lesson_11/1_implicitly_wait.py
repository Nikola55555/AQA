from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(10)            # Указание неявного ожидания
driver.get('https://demoqa.com/dynamic-properties')

VIZIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VIZIBLE_AFTER_BUTTON).click()
driver.close()