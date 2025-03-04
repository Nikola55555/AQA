import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

#driver.get('https://test-shop.qa.studio')
driver.get('https://test-shop.qa.studio/product-category/%d0%b8%d0%bd%d1%82%d0%b5%d1%80%d1%8c%d0%b5%d1%80/%d0%b2%d0%b0%d0%b7%d1%8b/')
#driver.find_element("xpath", "//a[@class='button-link']").click()

#cookies = driver.get_cookies()
#pickle.dump(cookies, open(os.getcwd() + "\lesson_14\cookies\cookies.pkl", "wb"))

driver.delete_all_cookies()

time.sleep(5)

#driver.refresh()
cookies = pickle.load(open(os.getcwd() + "\lesson_14\cookies\cookies.pkl", "rb"))

for cookie in cookies:
     driver.add_cookie(cookie)

driver.refresh()

time.sleep(5)


#driver.delete_all_cookies()  # Перед добавлением кук, необходимо очистить от старых кук, иначе не будет работать

#driver.get_cookies()  # Получение всех кук со страницы (можно сохранить в переменную)

#pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))  # Сохраняем куки в файл (что?, куда?, как?), wb - запись

# cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))  # Загружаем сохраненные куки в переменную, rb - чтение
# for cookie in cookies:
#     driver.add_cookie(cookie)

# driver.refresh() # Обязательно сделать рефреш, чтобы применились куки



# time.sleep(5)
# print(driver.get_cookies())


