from .pages.main_page import MainPage

link="http://selenium1py.pythonanywhere.com/"

def test_should_be_login_link(browser):
    page=MainPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page=MainPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page()
    

