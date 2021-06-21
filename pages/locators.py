#
from selenium.webdriver.common.by import By

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".row .col-sm-6 h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)>div strong")
    PRICE_PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)>.alertinner p strong")
    MESSAGE_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)>div")
    MESSAGE_OF_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)>.alertinner p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages div .alertinner")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID =(By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
