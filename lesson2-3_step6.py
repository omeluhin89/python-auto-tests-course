from selenium import webdriver
import time
import os
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value')
    x = x.text
    x = int(x)
    y = calc(x)
    y = str(y)
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    submit1 = browser.find_element_by_css_selector('[type="submit"]')
    submit1.click()

finally:
    time.sleep(5)
    browser.quit()
