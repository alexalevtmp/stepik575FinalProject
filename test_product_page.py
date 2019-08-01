from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators # ADD_TO_CART

# locators.py
# class ProductPageLocators(object):
#     ADD_TO_CART = (By.CSS_SELECTOR, "btn-add-to-basket")


# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    
    # add_to_cart()