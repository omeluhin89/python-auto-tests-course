import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_send_answer(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    input_answer = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
    answer = math.log(int(time.time()))
    answer = str(answer)
    input_answer.send_keys(answer)
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    fitback = browser.find_element_by_css_selector('.smart-hints__hint')
    text = fitback.text
    print(text)
    assert text == 'Correct!', "Answer is not right!"
