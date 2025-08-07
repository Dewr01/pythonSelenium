import pytest
from pages.product_page import ProductPage


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page.should_be_empty_basket()
