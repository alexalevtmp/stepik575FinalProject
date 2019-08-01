from .base_page import BasePage
from .locators import ProductPageLocators
# from .locators import MainPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        login_link.click()
        self.solve_quiz_and_get_code()        
        # pass

    def guest_can_add_product_to_cart(self):
        pass


# class MainPage(BasePage):
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         login_link.click()

#     # def should_be_login_link(self):
#     #     assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"

#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

