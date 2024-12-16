import pytest
from .pages.product_page import ProductPage


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



