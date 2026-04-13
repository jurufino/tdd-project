from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title

inputbox = browser.find_element("tag name", "input")
assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

# PRIMEIRO ITEM
inputbox.send_keys('Buy milk')
inputbox.send_keys(Keys.ENTER)

assert '1: Buy milk' in browser.page_source

# SEGUNDO ITEM
inputbox = browser.find_element("tag name", "input")
inputbox.send_keys('Make coffee')
inputbox.send_keys(Keys.ENTER)

assert '2: Make coffee' in browser.page_source

browser.quit()