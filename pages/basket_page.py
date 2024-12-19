from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_is_basket_empty(self):
        self.should_be_empty_basket_message()
        self.should_be_empty_basket()
    
    def should_be_empty_basket_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert 'empty' in empty_message, "There is no message about basket emptiness"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket item(s) is/are presented, but should not be"
        
