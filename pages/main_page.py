from .base_page import BasePage
# from selenium.webdriver.common.by import By
from .locators import MainPageLocators

from .login_page import LoginPage
from .locators import LoginPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        # *MainPageLocators.LOGIN_LINK
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        # login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        login_link.click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

