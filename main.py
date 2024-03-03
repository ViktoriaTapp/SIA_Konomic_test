from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import logging

logger = logging.getLogger(__file__)

import time

ROOT_DIR = Path(__file__).parent


CHROME_WEBDRIVER_PATH = ROOT_DIR / "chrome_driver/chromedriver"
URL = "https://exchange.konomik.com/authorization/signup"

options = webdriver.ChromeOptions()



try:
    service = Service(executable_path=CHROME_WEBDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url=URL)
    shadow_host = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "remoteComponent")))
    shadow_root = shadow_host.shadow_root

    username = driver.execute_script(
        'return document' +
        '.querySelector(\'.remoteComponent\')' +
        '.shadowRoot' +
        '.querySelector(\'[data-wi="user-name"]\')' +
        '.querySelector(\'[specialtoken="k-text-field-primary"]\')'
    )
    username.send_keys("AAA")
    
    email = shadow_root.find_element(By.NAME, 'username')
    email.send_keys("AAAA")


    input_password = shadow_root.find_element(By.ID, 'new-password')
    input_password.send_keys("AAA")
    time.sleep(20)

except Exception as ex:
    logger.error(f"Got error when trying to test {ex}")
finally:
    driver.quit()