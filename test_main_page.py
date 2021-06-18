#
from .pages.basket_page import BasketPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.chek_basket_empty()
    page.should_see_message_empty_basket()
