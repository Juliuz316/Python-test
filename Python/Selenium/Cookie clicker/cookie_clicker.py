from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

pause = False

cookie_id = "bigCookie"
cookies_prompt = "fc-button fc-cta-consent fc-primary-button"

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookies_prompt_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Consent')]")
time.sleep(3)
cookies_prompt_element.click()

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
time.sleep(1)
language.click()
time.sleep(4)

cookie_click = driver.find_element(By.ID, cookie_id)

while True:

    if keyboard.is_pressed("P"):  # Press keyboard P for pause, press it again to unpause
        keyboard.wait('P', suppress=True)
        time.sleep(1)

    cookie_click.click()
    cookie_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))

    for i in range(19):
        product_price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookie_count >= product_price:
            product = driver.find_element(By.ID, "product" + str(i))
            product.click()
            break
