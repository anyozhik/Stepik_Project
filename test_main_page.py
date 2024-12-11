from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link="http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser, link) #инициализируем PageObject, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page()
    
