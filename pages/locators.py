from selenium.webdriver.common.by import By

#Каждый класс будет соответствовать каждому классу PageObject: 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BTN=(By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    BOOK_TITLE=(By.CSS_SELECTOR, ".col-sm-6 h1")
    BOOK_PRICE=(By.CSS_SELECTOR, ".col-sm-6 .price_color")
    BOOK_TITLE_2=(By.CSS_SELECTOR, "#messages strong")
    BOOK_PRICE_2=(By.CSS_SELECTOR, "div[class='alertinner '] p strong")


 

    
