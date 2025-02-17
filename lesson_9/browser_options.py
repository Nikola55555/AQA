import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'  # Указываем стратегиюзагрузки страницы (normal, eager)
#chrome_options.add_argument('--headless') # Включение опции безголового режима
# chrome_options.add_argument('--incognito') # Включение режима Инкогнито
# chrome_options.add_argument('--ignore-certificate-errors') # Включение опции игнорирования сертификатов
chrome_options.add_argument('--window-size=700,700') # Установка размера окна
# chrome_options.add_argument('--disable_cache') # Отключение кэширования
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()

driver.get("https://whatismyipadress.com")

end_time = time.time()
result = end_time - start_time
print(result)