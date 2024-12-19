import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}/?promo=offer{no}" if no !=7
        else pytest.param("bugged_link", marks=pytest.mark.xfail)
        for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page=ProductPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_title()
    page.check_amount()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page=ProductPage(browser, link) 
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page=ProductPage(browser, link) 
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail  
def test_message_diappeared_after_adding_product_to_basket(browser):
    page=ProductPage(browser, link) 
    page.open()
    page.add_to_basket()
    page.should_success_message_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser, link) 
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


