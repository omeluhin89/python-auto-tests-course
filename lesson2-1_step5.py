from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    browser.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(30)
    browser.quit()
