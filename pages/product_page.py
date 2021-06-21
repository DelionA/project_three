#
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_product_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()

    def should_be_message_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET) , \
                                              "message of product add to basket not present"
        message_product_add_to_card = \
            self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET).text
        print(message_product_add_to_card)
        message_product_name = \
            self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message_product_name == product_name, \
                                 "product name in message of add to basket not match"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_OF_PRICE_BASKET), \
                                               "message of price basket not present"
        message_price_basket = \
            self.browser.find_element(*ProductPageLocators.MESSAGE_OF_PRICE_BASKET).text
        print(message_price_basket)
        price_product_message = \
            self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_product_message == price_product, \
                                      "product price in message of add to basket not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET), \
                                               "Sucess message is presented, but should not be"

    def should_see_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET), \
                                              "Success message present, but should not be"
