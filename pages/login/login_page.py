from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

# import this log if you want to print this class "LoginPage" in the logs
# from utilities import custom_logger as cl
# import logging
# put this code before __init__ below -> log = cl.custom_logger(logging.DEBUG)

class LoginPage(SeleniumDriver): # inherit SeleniumDriver

    # log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver) and providing the driver
        self.driver = driver

    # Locators
    _email_field = "//input[@name='username']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[normalize-space()='Login']"



    # GET ELEMENT METHODS --------------------------------------------------------------------------------------------
    # No Longer Needed -> since SeleniumDriver class has this functions getting the element
    # def get_username_field(self):
    #     return self.driver.find_element(By.XPATH, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.XPATH, self._password_field)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)


    # ACTION ---------------------------------------------------------------------------------------------------------
    def enter_username(self, email):
        # self.get_username_field().send_keys(email)
        self.send_text(email, self._email_field) # locator_type optional -> default value is xpath

    def enter_password(self, password):
        # self.get_password_field().send_keys(password)
        self.send_text(password, self._password_field)

    def click_login_button(self):
        # self.get_login_button().click()
        self.element_click(self._login_button)




    # METHODS---------------------------------------------------------------------------------------------------------
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
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

