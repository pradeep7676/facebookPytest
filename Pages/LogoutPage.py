from selenium.webdriver.common.by import By


class LogoutPage:

    '''locators'''
    ACCOUNT = (By.XPATH, "//div[@class='qi72231t o9w3sbdw nu7423ey tav9wjvu flwp5yud tghlliq5 gkg15gwv s9ok87oh s9ljgwtm lxqftegz bf1zulr9 frfouenu bonavkto djs4p424 r7bn319e bdao358l fsf7x5fv tgm57n0e jez8cy9q s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk dnr7xe2t aeinzg81 srn514ro oxkhqvkx rl78xhln nch0832m om3e55n1 cr00lzj9 rn8ck1ys s3jn8y49 g4tp4svg o9erhkwx dzqi5evh hupbnkgi hvb2xoa8 jl2a5g8c f14ij5to l3ldwz01 icdlwmnq pbevjfx6 aglvbi8b']//div[@class='aglvbi8b om3e55n1 i8zpp7h3 g4tp4svg']//*[name()='svg']//*[name()='g' and contains(@mask,'url(#jsc_c')]//*[name()='image' and contains(@x,'0')]")
    LOGOUT = (By.XPATH, "//span[text()='Log Out']")

    def __init__(self, driver):
        self.driver = driver

    def account(self):
        return self.driver.find_element(*LogoutPage.ACCOUNT)

    def logout(self):
        return self.driver.find_element(*LogoutPage.LOGOUT)