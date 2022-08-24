from selenium.webdriver.common.by import By


class LoginPage:

    '''locators'''
    USER_NAME = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")

    def __init__(self, driver):
        self.driver = driver

    def user_name(self):
        return self.driver.find_element(*LoginPage.USER_NAME)

    def password(self):
        return self.driver.find_element(*LoginPage.PASSWORD)

    def login_button(self):
        return self.driver.find_element(*LoginPage.LOGIN_BUTTON)



