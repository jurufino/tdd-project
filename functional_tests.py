from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

try:
    # Usuário entra no site
    browser.get('http://localhost:8000')

    assert 'To-Do' in browser.title

    # Encontra o input
    inputbox = browser.find_element(By.TAG_NAME, 'input')
    assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

    # Digita um item
    inputbox.send_keys('Buy milk')
    inputbox.send_keys(Keys.ENTER)

    time.sleep(1)

    # Verifica se foi redirecionado para /lists/1
    assert '/lists/' in browser.current_url

    # Verifica se o item apareceu
    body_text = browser.find_element(By.TAG_NAME, 'body').text
    assert '1: Buy milk' in body_text

finally:
    browser.quit()