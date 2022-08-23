from selenium.webdriver.common.by import By

class ProfilePage:

    PROFILE_NAME = (By.XPATH,"//span[text()='Pradeep Reddy']")

    def __init__(self, driver):
        self.driver = driver

    def profile_name(self):
        return self.driver.find_element(*ProfilePage.PROFILE_NAME)