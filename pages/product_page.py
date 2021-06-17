
from .base_page import BasePage
#from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
    def add_product_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        time.sleep(5)
        product_name_and_price_card = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_AND_PRICE_CARD)
        product_name_card = product_name_and_price_card[0].text
        product_price_card = product_name_and_price_card[2].text
        assert product_name_card == product_name, f"product name not match, expected {product_name}"
        assert product_price_card == product_price, f"product price not math, expected {product_price}"
        print(f"\n{product_name_card} has been added to your basket.")
        print(f"\nyour basket total is now {product_price_card}.")
        
        
        
