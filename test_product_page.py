#
import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

link_login = "http://selenium1py.pythonanywhere.com/accounts/login/"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_offer = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_offer)
    page.open()
    page.add_product_to_card()
    page.solve_quiz_and_get_code()
    page.should_be_message_add_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_card()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_card()
    page.should_see_success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.chek_basket_empty()
    page.should_see_message_empty_basket()

@pytest.mark.user_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function",autouse=True)
    def setup(self, browser):
        page = LoginPage(browser,link_login)
        page.open()
        email = str(time.time()) + "@yandex.mnu"
        password = "C67dawHXppx7Sux"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_offer)
        page.open()
        page.add_product_to_card()
        page.solve_quiz_and_get_code()
        page.should_be_message_add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
