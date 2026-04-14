from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_can_start_a_list_and_retrieve_it_later():
    browser = webdriver.Chrome()

    browser.get('http://127.0.0.1:8000')

    inputbox = browser.find_element(By.TAG_NAME, 'input')

    inputbox.send_keys('Comprar pão')
    inputbox.send_keys(Keys.ENTER)

    time.sleep(5)
    browser.quit()

    assert '/lists/' in browser.current_url

    table = browser.find_element(By.TAG_NAME, 'body')
    assert 'Comprar pão' in table.text

    browser.get('http://127.0.0.1:8000')

    inputbox = browser.find_element(By.TAG_NAME, 'input')
    inputbox.send_keys('Estudar Django')
    inputbox.send_keys(Keys.ENTER)

    time.sleep(5)
    browser.quit()

    new_url = browser.current_url
    assert new_url != 'http://127.0.0.1:8000/lists/1/'

    body = browser.find_element(By.TAG_NAME, 'body')
    assert 'Estudar Django' in body.text

    browser.quit()


if __name__ == "__main__":
    test_can_start_a_list_and_retrieve_it_later()