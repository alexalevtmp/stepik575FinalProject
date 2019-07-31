from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

# link = "http://selenium1py.pythonanywhere.com/"

# link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

# def test_guest_should_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()



# # Второй подход: переход происходит неявно, страницу инициализируем в теле теста: 
# # 1. Закомментируйте строку с возвращаемым значением 

def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url) 

# # 2. Инициализируем LoginPage в теле теста (не забудьте импортировать в файл нужный класс): 

# # from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



## from prev step!
# def test_should_be_login_page(browser):
#     page = LoginPage(browser, link_login)
#     page.open()
#     page.should_be_login_page()


# "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

# "http://selenium1py.pythonanywhere.com/"
# "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


# Wed Jul 31 20:36:11 UTC 2019
# (selenium_env) bash-3.2$ pytest -v --tb=line --language=en test_main_page.py
# ============================================================ test session starts =============================================================
# platform darwin -- Python 3.7.3, pytest-3.10.1, py-1.8.0, pluggy-0.12.0 -- /anaconda3/envs/selenium_env/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/asl/stepik575/stepik575FinalProject, inifile:
# plugins: rerunfailures-3.1
# collected 3 items                                                                                                                            

# test_main_page.py::test_guest_can_go_to_login_page PASSED                                                                              [ 33%]
# test_main_page.py::test_guest_should_see_login_link PASSED                                                                             [ 66%]
# test_main_page.py::test_should_be_login_page PASSED                                                                                    [100%]

# ========================================================= 3 passed in 12.95 seconds ==========================================================
