import time
import traceback

from Config.confiq import TestData
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage
from Pages.ProfilePage import ProfilePage
from Pages.SettingsPage import SettingsPage
from utilities.BasePage import BasePage


class Test_e2e(BasePage):

    def test_verify_LoginPage_title(self):
        self.driver.implicitly_wait(10)
        '''to verify login page'''
        login_page_title = self.driver.title
        assert login_page_title == TestData.LOGIN_PAGE_TITLE
        self.message_logging("title verified succesfully")

    def test_login(self, params):
        '''objcet for loginpage'''
        login_page = LoginPage(self.driver)
        '''to enter username and password through terminal'''
        login_page.user_name().send_keys(params['username'])
        login_page.password().send_keys(params['password'])
        self.waiting_until_item_enabled( login_page.login_button())
        login_page.login_button().click()
        self.message_logging("login successfully")

    def test_verify_profilePage_title(self):
        profile_page_title = self.driver.title
        '''to verify profile page title after login'''
        try:
            if profile_page_title == TestData.PROFILE_PAGE_TITLE:
                self.message_logging("successfully verified the profile page title")
            elif profile_page_title == TestData.PROFILE_PAGE_TITLE2:
                self.message_logging("succesfully verifeid profile page title")

        except AssertionError:
            print(traceback.format_exc())


    def test_verify_profile_name(self):
        profilePage = ProfilePage(self.driver)
        '''to verify profile name'''
        name = profilePage.profile_name().text
        assert name == TestData.PROFILE_NAME
        self.message_logging("profile name verified successfully")

    def test_settings(self):
        setting_page = SettingsPage(self.driver)
        '''to click on account'''
        setting_page.click_account().click()

        '''to click on settings and privacy'''
        setting_page.click_settings_privacy().click()

        '''To click on setting '''
        setting_page.click_setting().click()

        '''To click on privacy'''
        setting_page.click_privacy().click()

        time.sleep(2)
        '''to click on manage profile after switching to frames'''
        setting_page.click_manage_profile().click()

        time.sleep(2)
        '''to verify phone number'''
        number = setting_page.click_number_verify().text
        self.message_logging(number)
        assert number == TestData.NUMBER_VERIFY
        self.driver.back()
        self.message_logging("mobile number verified successfully")

        '''To click on blocking'''
        setting_page.click_blocking().click()

        '''To click on edit button'''
        setting_page.click_edit().click()

        '''To click on blocked list'''
        setting_page.click_blockedList().click()

        '''to get list of blocked user'''
        total_no_blocks = setting_page.blocks()
        blocks = len(total_no_blocks)
        self.message_logging(blocks)
        setting_page.close_list().click()
        self.message_logging("successfully got the total number of blocked users")

    def test_logout(self):
        logout_obj = LogoutPage(self.driver)
        '''To click on account'''
        logout_obj.account().click()
        '''to click on logout'''
        logout_obj.logout().click()
        self.message_logging("logout successfully")







