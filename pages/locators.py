from selenium.webdriver.common.by import By

#Каждый класс будет соответствовать каждому классу PageObject: 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID=(By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD=(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD1=(By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD2=(By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON=(By.CSS_SELECTOR, "button[value='Register']")

    

class ProductPageLocators():
    BASKET_BTN=(By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    BOOK_TITLE=(By.CSS_SELECTOR, ".col-sm-6 h1")
    BOOK_PRICE=(By.CSS_SELECTOR, ".col-sm-6 .price_color")
    BOOK_TITLE_2=(By.CSS_SELECTOR, "#messages strong")
    BOOK_PRICE_2=(By.CSS_SELECTOR, "div[class='alertinner '] p strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(1)")


class BasketPageLocators():
    EMPTY_MESSAGE=(By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM=(By.CSS_SELECTOR, ".basket-items")
    

 

    
