from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class SettingsPage(BasePage):

    '''locators'''
    ACCOUNT = (By.XPATH, "//div[@class='qi72231t o9w3sbdw nu7423ey tav9wjvu flwp5yud tghlliq5 gkg15gwv s9ok87oh s9ljgwtm lxqftegz bf1zulr9 frfouenu bonavkto djs4p424 r7bn319e bdao358l fsf7x5fv tgm57n0e jez8cy9q s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk dnr7xe2t aeinzg81 srn514ro oxkhqvkx rl78xhln nch0832m om3e55n1 cr00lzj9 rn8ck1ys s3jn8y49 g4tp4svg o9erhkwx dzqi5evh hupbnkgi hvb2xoa8 jl2a5g8c f14ij5to l3ldwz01 icdlwmnq pbevjfx6 aglvbi8b']//div[@class='aglvbi8b om3e55n1 i8zpp7h3 g4tp4svg']//*[name()='svg']//*[name()='g' and contains(@mask,'url(#jsc_c')]//*[name()='image' and contains(@x,'0')]")
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
        self.wait_clickable(SettingsPage.ACCOUNT)
        return self.driver.find_element(*SettingsPage.ACCOUNT)

    def click_settings_privacy(self):
        self.wait_clickable(SettingsPage.SETTING_PRIVACY)
        return self.driver.find_element(*SettingsPage.SETTING_PRIVACY)

    def click_setting(self):
        self.wait_clickable(SettingsPage.SETTING)
        return self.driver.find_element(*SettingsPage.SETTING)

    def click_privacy(self):
        self.wait_clickable(SettingsPage.PRIVACY)
        return self.driver.find_element(*SettingsPage.PRIVACY)

    def click_manage_profile(self):
        '''switch to frame'''
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        return self.driver.find_element(*SettingsPage.MANAGE_PROFILE)

    def click_number_verify(self):
        return self.driver.find_element(*SettingsPage.NUMBER_VERIFY)

    def click_blocking(self):
        self.wait_clickable(SettingsPage.BLOCKING)
        return self.driver.find_element(*SettingsPage.BLOCKING)

    def click_edit(self):
        self.wait_clickable(SettingsPage.EDIT)
        return self.driver.find_element(*SettingsPage.EDIT)

    def click_blockedList(self):
        self.wait_clickable(SettingsPage.BLOCKEDLIST)
        return self.driver.find_element(*SettingsPage.BLOCKEDLIST)

    def blocks(self):
        self.wait_presence(SettingsPage.TOTAL_NO_BLOCKS)
        return self.driver.find_elements(*SettingsPage.TOTAL_NO_BLOCKS)

    def close_list(self):
        self.wait_clickable(SettingsPage.CLOSE_LIST)
        return self.driver.find_element(*SettingsPage.CLOSE_LIST)
