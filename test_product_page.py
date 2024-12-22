import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import faker
f = faker.Faker()

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}/?promo=offer{no}" if no !=7
        else pytest.param("bugged_link", marks=pytest.mark.xfail)
        for no in range(10)]

@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page=ProductPage(browser, link) 
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
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page=ProductPage(browser, link) 
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page=ProductPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = f.email()
        password=f.password()
        page=ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page=LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
 
    def test_user_cant_see_success_message(self, browser):
        page=ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page=ProductPage(browser, link) 
        page.open()
        page.add_to_basket()
        page.check_title()
        page.check_amount()






