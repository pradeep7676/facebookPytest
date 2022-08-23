from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

from Config.confiq import TestData


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'USER_NAME': ('ID', "email"),
        'PASSWORD': ('ID', "pass"),
        'LOGIN_BUTTON': ('XPATH', "//button[text()='Log In']")
    }

    '''USER_NAME = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")'''



    '''def user_name(self):
        return self.driver.find_element(*LoginPage.USER_NAME)

    def password(self):
        return self.driver.find_element(*LoginPage.PASSWORD)

    def login_button(self):
        return self.driver.find_element(*LoginPage.LOGIN_BUTTON)'''

    def enter_username(self):
        self.USER_NAME.set_text("pradepreddy1994@gmail.com")

