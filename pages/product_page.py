from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def check_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_title2 = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_2).text
        assert book_title == book_title2, f'Expected {book_title}, get {book_title2}'

    def check_amount(self):
        book_price=self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price2=self.browser.find_element(*ProductPageLocators.BOOK_PRICE_2).text
        assert book_price == book_price2, f'Expected {book_price}, get {book_price2}'


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is not disappeared"


