from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--window-size=1920,1080')
#options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

FULL_NAME_LOCATOR = ("xpath", "//input[@id='userName']")
EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")
BUTTON_SUBMIT = ("xpath", "//button[@id='submit']")
ASSERT_AREA_NAME = ("xpath", "//p[@id='name']")
ASSERT_AREA_EMAIL = ("xpath", "//p[@id='email']")

expected_value_name = 'Николай'
expected_value_email = 'bagbee84@mail.ru'

driver.get('https://demoqa.com/text-box')

driver.find_element(*FULL_NAME_LOCATOR).send_keys(expected_value_name)
driver.find_element(*EMAIL_FIELD).send_keys(expected_value_email)
driver.find_element(*CURRENT_ADDRESS).send_keys("Привет! Как дела?")
driver.find_element(*PERMANENT_ADDRESS).send_keys("Тут будет текст с адресом")
driver.find_element(*BUTTON_SUBMIT).click()

time.sleep(5)

actual_value_name = driver.find_element(*ASSERT_AREA_NAME).text
actual_value_email = driver.find_element(*ASSERT_AREA_EMAIL).text

name_text = actual_value_name.replace("Name:", "").strip()
#assert  name_text == expected_value_name, f"Ожидалось {expected_value_name}, получено {name_text}"
email_text = actual_value_email.replace("Email:", "").strip()

def test_name_field():
    assert name_text == expected_value_name, f"Ожидалось {expected_value_name}, получено {name_text}"

def test_email_field():
    assert email_text == expected_value_email, f'Ожидалось {expected_value_email}, получено {email_text}'
