"""
Functional testing for selenium webdriver on Firefox browser.
Obeying the testing goat
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Congratulations!' in browser.title