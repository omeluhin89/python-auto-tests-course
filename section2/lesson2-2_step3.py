from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    num1 = browser.find_element_by_id('num1')
    num1 = num1.text
    num2 = browser.find_element_by_id('num2')
    num2 = num2.text
    sum = int(num1) + int(num2)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(sum))
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
