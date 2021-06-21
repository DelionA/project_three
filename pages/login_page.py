#
from .base_page import BasePage
from .locators import BasePageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*BasePageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*BasePageLocators.REGISTER_FORM_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*BasePageLocators.REGISTER_BUTTON).click()
