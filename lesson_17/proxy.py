from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROXY_SERVER = 'username:password@37.19.220.129:8443'  # Если логига и пароля нет, то прописываем только IP адрес

option = Options()
option.add_argument(f"--proxy-server={PROXY_SERVER}")
driver = webdriver.Chrome(options=option)
driver.get("https://2ip.ru")