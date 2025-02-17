import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\Downloads"   # Указываем в pref куда сщхранять скачанные файлы
}
chrome_options.add_experimental_option("prefs", prefs)  #  Добовляем prefs  в опции
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/download')
time.sleep(3)

driver.find_elements("xpath", "//a")[3].click()   # Ищем элемент с помощью xpath и по тегу a находим все эдементы и
                                                            # кликаем на 3й элемент

time.sleep(3)
