from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super.__init__(driver)  # calling __init__ method of superclass (SeleniumDriver) and providing the driver
        self.driver = driver

    # Locators
    _email_field = "//input[@name='username']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[normalize-space()='Login']"


    # GET ELEMENT METHODS =============================================================================================
    def get_username_field(self):
        return self.driver.find_element(By.XPATH, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.XPATH, self._password_field)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self._login_button)


    # ACTION METHODS ==================================================================================================
    def click_login_button(self):
        self.get_login_button().click()

    def username(self, email):
        self.get_username_field().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)


    # STEPS ===========================================================================================================
    # def login(self, username, password):
        # email_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # email_field.send_keys(username)
        #
        # password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password_field.send_keys(password)
        #
        # login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        # login_button.click()

    def login(self, username, password):
        self.username(username)
        self.enter_password(password)
        self.click_login_button()

