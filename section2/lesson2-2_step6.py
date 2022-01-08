from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')
    x = browser.find_element_by_id('input_value')
    x = x.text
    x = int(x)
    y = calc(x)
    y = str(y)
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    browser.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(5)
    browser.quit()
