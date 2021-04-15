from selenium.webdriver.common.by import By


class LogOutPage:
    link_logout_xpath = "/html/body/section/section/div[1]/div/ul/li/a"
    div_user_class = "user"

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def click_username(self):
        self.driver.find_element(By.CLASS_NAME, self.div_user_class).click()