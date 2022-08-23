from selenium.webdriver.common.by import By

class LogoutPage:
    ACCOUNT = (By.XPATH, "//div[@class='alzwoclg om3e55n1']")
    LOGOUT = (By.XPATH, "//span[text()='Log Out']")


    def __init__(self, driver):
        self.driver = driver

    def account(self):
        return self.driver.find_element(*LogoutPage.ACCOUNT)

    def logout(self):
        return self.driver.find_element(*LogoutPage.LOGOUT)