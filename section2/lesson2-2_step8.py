from selenium import webdriver
import time
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("test@test.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    fileSelector = browser.find_element_by_id('file')
    fileSelector.send_keys(file_path)
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
