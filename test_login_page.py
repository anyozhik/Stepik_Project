from .pages.login_page import LoginPage

link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
word="login"

def test_should_be_login_url(browser):
    page=LoginPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_be_login_url(link, word)

def test_should_be_login_form(browser):
    page=LoginPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_be_login_form()
    
def test_should_be_register_form(browser):
    page=LoginPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_be_register_form()

