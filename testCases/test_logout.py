import pytest
from pageObjects.LogOutPage import LogOutPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test001Logout:
    baseURL = ReadConfig.get_application_url() + '/login'
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, setup):

        self.logger.info("****Started Logout Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.log_out = LogOutPage(self.driver)
        self.log_out.click_username()
        self.log_out.click_logout()
        name = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/p[2]/a[1]').text

        if name == "Login":
            self.logger.info("****Logout test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Logout test failed ****")
            self.driver.save_screenshot(".\\screenshots\\" + "logoutPage.png")
            self.driver.close()
            assert False
