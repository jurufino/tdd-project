from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    # Abrir home
    browser.get('http://127.0.0.1:8000')

    # Encontrar input e enviar vazio
    inputbox = browser.find_element(By.NAME, 'item_text')
    inputbox.send_keys('')
    inputbox.submit()

    time.sleep(1)

    # Verificar se mensagem de erro aparece
    body_text = browser.find_element(By.TAG_NAME, 'body').text

    assert "Você não pode enviar um item vazio" in body_text

finally:
    time.sleep(5)
    browser.quit()