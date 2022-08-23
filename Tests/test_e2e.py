import time
import traceback

from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

from Config.confiq import TestData
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage
from Pages.ProfilePage import ProfilePage
from Pages.SettingsPage import SettingsPage
from utilities.BasePage import BasePage


class Test_e2e(BasePage):

    def test_verify_LoginPage_title(self):
        self.driver.implicitly_wait(10)
        try:
            login_page_title = self.driver.title
             #to verify loginPage title
            assert login_page_title == TestData.LOGIN_PAGE_TITLE
        except AssertionError:
            print(traceback.format_exc())
        self.message_logging("title verified succesfully")

    def test_login(self):
        login_page = LoginPage(self.driver)
        #to enter username and password
        login_page.enter_username()
        login_page.password().send_keys(TestData.PASSWORD)
        login_page.login_button().click()
        self.message_logging("login successfully")

    def test_verify_profilePage_title(self):
        profile_page_title = self.driver.title
        #to verify profile page title after login
        assert profile_page_title == TestData.PROFILE_PAGE_TITLE
        self.message_logging("profile page title verified")

    def test_verify_profile_name(self):
        profilePage = ProfilePage(self.driver)
        #to verify profile name
        name = profilePage.profile_name().text
        assert name == TestData.PROFILE_NAME
        self.message_logging("profile name verified successfully")

    def test_settings(self):
        setting_page = SettingsPage(self.driver)
        #to click on account
        setting_page.click_account().click()
        # to click on settings and privacy
        self.wait_clickable(SettingsPage.SETTING_PRIVACY)
        setting_page.click_settings_privacy().click()
        #to click on settings

        self.wait_clickable(SettingsPage.SETTING)
        setting_page.click_setting().click()
        #to click on privacy
        setting_page.click_privacy().click()

        time.sleep(2)
        #self.wait_presence(SettingsPage.SETTING)
        setting_page.click_manage_profile().click()

        time.sleep(2)
        #self.wait_presence(SettingsPage.NUMBER_VERIFY)
        number = setting_page.click_number_verify().text
        assert number == TestData.NUMBER_VERIFY
        self.driver.back()
        self.message_logging("mobile number verified successfully")

        #to click blocking
        setting_page.click_blocking().click()

        #to click on edit button
        setting_page.click_edit().click()

        #to click on blocked list
        setting_page.click_blockedList().click()

        # to get list of blocked user
        total_no_blocks = setting_page.blocks()
        blocks = len(total_no_blocks)
        print("total number of blocked users:",blocks)
        setting_page.close_list().click()
        self.message_logging("successfully got the total number of blocked users")

    def test_logout(self):
        logout_obj = LogoutPage(self.driver)
        logout_obj.account().click()
        logout_obj.logout().click()
        self.message_logging("logout successfully")




