from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

try:
    # Usuário A entra no site
    browser.get('http://localhost:8000')

    inputbox = browser.find_element(By.TAG_NAME, 'input')
    inputbox.send_keys('Buy milk')
    inputbox.send_keys(Keys.ENTER)

    time.sleep(1)

    # Pega a URL da lista do usuário A
    user_a_url = browser.current_url
    assert '/lists/' in user_a_url

    # Verifica item
    body_text = browser.find_element(By.TAG_NAME, 'body').text
    assert 'Buy milk' in body_text

    # Agora simula um novo usuário (nova sessão)
    browser.quit()
    browser = webdriver.Firefox()

    # Usuário B entra no site
    browser.get('http://localhost:8000')

    body_text = browser.find_element(By.TAG_NAME, 'body').text
    assert 'Buy milk' not in body_text  # NÃO pode ver a lista do A

    # Usuário B cria nova lista
    inputbox = browser.find_element(By.TAG_NAME, 'input')
    inputbox.send_keys('Make coffee')
    inputbox.send_keys(Keys.ENTER)

    time.sleep(1)

    user_b_url = browser.current_url
    assert '/lists/' in user_b_url

    # URLs devem ser diferentes
    assert user_a_url != user_b_url

    body_text = browser.find_element(By.TAG_NAME, 'body').text
    assert 'Make coffee' in body_text
    assert 'Buy milk' not in body_text

finally:
    browser.quit()