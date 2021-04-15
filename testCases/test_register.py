import pytest
from pageObjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test001Register:
    baseURL = ReadConfig.get_application_url() + '/register'
    email = ReadConfig.get_email()
    name = ReadConfig.get_name()
    username = ReadConfig.get_username()
    avatar_url = ReadConfig.get_avatar_url()
    password = ReadConfig.get_password()
    logger = LogGen.logger()

    @pytest.mark.regression
    def test_login_page_title(self, setup):
        self.logger.info("*************** Test_001_Register *****************")
        self.logger.info("****Started Register page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        title = self.driver.title
        print(title)
        if title == "Calendar App":
            self.logger.info("**** Register page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Register page title test failed****")
            self.driver.save_screenshot(".\\screenshots\\" + "registerPageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register(self, setup):
        self.logger.info("****Started Register Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.set_email(self.email)
        self.registerPage.set_name(self.name)
        self.registerPage.set_username(self.username)
        self.registerPage.set_avatar_url(self.avatar_url)
        self.registerPage.set_password(self.password)
        self.registerPage.click_register()
        message = self.driver.find_element(By.XPATH, '/html/body/div[2]/form/p/a').text

        if message == "Already registered":
            self.logger.info("****Register test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Register test failed ****")
            self.driver.save_screenshot(".\\screenshots\\" + "registerPage.png")
            self.driver.close()
            assert False
