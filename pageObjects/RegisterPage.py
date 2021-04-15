from selenium.webdriver.common.by import By


class RegisterPage:
    textbox_email_name = "email"
    textbox_name_name = "name"
    textbox_username_name = "username"
    textbox_password_name = "password"
    textbox_avatar_name = "image"
    button_register_xpath = "/html/body/div/form/button"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.NAME, self.textbox_email_name).clear()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email)

    def set_name(self, name):
        self.driver.find_element(By.NAME, self.textbox_name_name).clear()
        self.driver.find_element(By.NAME, self.textbox_name_name).send_keys(name)

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def set_avatar_url(self, avatar):
        self.driver.find_element(By.NAME, self.textbox_avatar_name).clear()
        self.driver.find_element(By.NAME, self.textbox_avatar_name).send_keys(avatar)

    def click_register(self):
        self.driver.find_element(By.XPATH, self.button_register_xpath).click()
