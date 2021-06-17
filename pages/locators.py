from selenium.webdriver.common.by import By

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_AND_PRICE_CARD = (By.CSS_SELECTOR, "#messages .alertinner strong")
    
