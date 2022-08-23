from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class SettingsPage(BasePage):

    ACCOUNT = (By.XPATH, "//div[@class='alzwoclg om3e55n1']")
    SETTING_PRIVACY = (By.XPATH, "//span[text()='Settings & privacy']")
    SETTING = (By.XPATH, "//span[text()='Settings']")
    PRIVACY = (By.XPATH,"//span[text()='Privacy']")
    MANAGE_PROFILE = (By.XPATH,"//div[normalize-space()='Manage your profile']")
    NUMBER_VERIFY = (By.XPATH,"(//div[@class='n3t5jt4f oog5qr5w k1z55t6l pbevjfx6 laatuukc'])[3]")
    BLOCKING = (By.XPATH,"//span[text()='Blocking']")
    EDIT = (By.XPATH,"(//div[@aria-label='Edit'])[2]")
    BLOCKEDLIST = (By.XPATH,"//span[text()='See your blocked list']")
    TOTAL_NO_BLOCKS = (By.XPATH,"//div[@class='h8391g91 m0cukt09 kpwa50dg ta68dy8c b6ax4al1']")
    CLOSE_LIST = (By.XPATH,"//div[@class='b0ur3jhr facqkgn9 s8sjc6am h28iztb5']")


    def __init__(self, driver):
        self.driver = driver

    def click_account(self):
        return self.driver.find_element(*SettingsPage.ACCOUNT)

    def click_settings_privacy(self):
        return self.driver.find_element(*SettingsPage.SETTING_PRIVACY)

    def click_setting(self):
        return self.driver.find_element(*SettingsPage.SETTING)

    def click_privacy(self):
        return self.driver.find_element(*SettingsPage.PRIVACY)

    def click_manage_profile(self):
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        return self.driver.find_element(*SettingsPage.MANAGE_PROFILE)

    def click_number_verify(self):
        return self.driver.find_element(*SettingsPage.NUMBER_VERIFY)

    def click_blocking(self):
        return self.driver.find_element(*SettingsPage.BLOCKING)

    def click_edit(self):
        return self.driver.find_element(*SettingsPage.EDIT)

    def click_blockedList(self):
        return self.driver.find_element(*SettingsPage.BLOCKEDLIST)

    def blocks(self):
        return self.driver.find_elements(*SettingsPage.TOTAL_NO_BLOCKS)

    def close_list(self):
        return self.driver.find_element(*SettingsPage.CLOSE_LIST)
