from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class LoginPage(BasePage):

    '''locators'''
    USER_NAME = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")

    def __init__(self, driver):
        self.driver = driver

    def user_name(self):
        self.wait_presence(LoginPage.USER_NAME)
        return self.driver.find_element(*LoginPage.USER_NAME)

    def password(self):
        self.wait_presence(LoginPage.PASSWORD)
        return self.driver.find_element(*LoginPage.PASSWORD)

    def login_button(self):
        self.wait_clickable(LoginPage.LOGIN_BUTTON)
        return self.driver.find_element(*LoginPage.LOGIN_BUTTON)



