import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org")

# url = driver.current_url # Получение URL страницы
# print("URL страницы: ", url)
# time.sleep(3)
#
# current_title = driver.title  # Получение Title страницы
# print("Title: ", current_title)
#
# assert url == "https://www.wikipedia.org", "Ошибка в URL, открыта не та страница."  # После запятой можно дать описание ощшибки
# assert current_title == "Wikipedia", "Ошибка в Title"
# ы
# time.sleep(3)

print(driver.page_source)   # Получения кода HTML страницы!