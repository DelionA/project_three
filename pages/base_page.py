#
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators, BasketPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            time.sleep(3)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login url incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM_EMAIL), \
                                               "email login form not found"
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM_PASSWORD), \
                                               "password login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*BasePageLocators.REGISTER_FORM_EMAIL), \
                                               "email register form not found"
        assert self.is_element_present(*BasePageLocators.REGISTER_FORM_PASSWORD), \
                                               "password register form not found"
        assert self.is_element_present(*BasePageLocators.REGISTER_FORM_PASSWORD_CONFIRM), \
                                                        "password_confirm form not found"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
