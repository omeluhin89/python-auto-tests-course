from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_button_card(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "add_to_basket_form"))
    )
