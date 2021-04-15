import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test001Login:
    baseURL = ReadConfig.get_application_url() + '/login'
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.logger()

    @pytest.mark.regression
    def test_login_page_title(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Login page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        title = self.driver.title
        print(title)
        if title == "Calendar App":
            self.logger.info("**** Login page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Login page title test failed****")
            self.driver.save_screenshot(".\\screenshots\\" + "loginPageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        name = self.driver.find_element(By.TAG_NAME, 'span').text

        if name == "SWAPNA SAMA":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\screenshots\\" + "loginPage.png")
            self.driver.close()
            assert False
