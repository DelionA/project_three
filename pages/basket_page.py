#
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def chek_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "basket not empty, but should be"
        
    def should_see_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "message of basket empty not present, but should bee present"
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert "Your basket is empty. Continue shopping" == basket_empty_message, "basket message of empty not correct"
