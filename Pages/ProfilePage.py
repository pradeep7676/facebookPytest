from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class ProfilePage(BasePage):
    '''locators'''
    PROFILE_NAME = (By.XPATH,"//span[text()='Pradeep Reddy']")

    def __init__(self, driver):
        self.driver = driver

    def profile_name(self):
        self.wait_presence(ProfilePage.PROFILE_NAME)
        return self.driver.find_element(*ProfilePage.PROFILE_NAME)