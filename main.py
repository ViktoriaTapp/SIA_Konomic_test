from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


WEBDRIVER_PATH = (
    "/Users/viktoriatappyrova/PycharmProjects/Selenium/chromedriver/chromedriver"
)
URL = "https://exchange.konomik.com/authorization/signup"

options = webdriver.ChromeOptions()


try:
    service = Service(executable_path=WEBDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url=URL)
    shadow_host = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "remoteComponent"))
    )
    shadow_root = shadow_host.shadow_root

    def send_username(username: str):
        js_code = """
        return document.querySelector('.remoteComponent').shadowRoot.querySelector('[data-wi="user-name"]').querySelector('[specialtoken="k-text-field-primary"]')
        """
        input_username = driver.execute_script(js_code)
        input_username.send_keys(username)

    def send_email(email: str):
        input_email = shadow_root.find_element(By.NAME, "username")
        input_email.send_keys(email)

    def send_password(password: str):
        input_password = shadow_root.find_element(By.ID, "new-password")
        input_password.send_keys(password)

    def send_referall_code(referral_code: str):
        js_code = """
        return document.querySelector('.remoteComponent').shadowRoot.querySelector('[data-wi="referral"]').querySelector('[specialtoken="k-text-field-primary"]')
        """
        input_referral_code_field = driver.execute_script(js_code)
        input_referral_code_field.send_keys(referral_code)

    def get_username_error_message():
        js_code = """
        return document.querySelector('.remoteComponent').shadowRoot.querySelector('[data-wi="user-name"]').querySelector('[data-wi="message"]').textContent.trim()
        """
        return driver.execute_script(js_code)

    def get_email_error_message():
        js_code = """
        return document.querySelector('.remoteComponent').shadowRoot.querySelector('[data-wi="identificator"]').querySelector('[data-wi="message"]').textContent.trim()
        """
        return driver.execute_script(js_code)


    def get_password_error_message():
        js_code = """
           return document.querySelector('.remoteComponent').shadowRoot.querySelector('[data-wi="password"]').querySelector('[data-wi="error"]').textContent.trim()
           """
        return driver.execute_script(js_code)

    send_username("q")
    send_email("")
    send_password("1")
    send_referall_code("12")
    # Sleep for setting values
    time.sleep(5)
    username_error_message = get_username_error_message()
    email_error_message = get_email_error_message()
    password_error_message = get_password_error_message()
    print(username_error_message, email_error_message, password_error_message)


except Exception as ex:
    print(ex)

finally:
    driver.quit()
