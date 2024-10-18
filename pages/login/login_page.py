import time
# from selenium.webdriver.common.by import By
# from base.selenium_driver import SeleniumDriver

# -> import this log if you want to print this class "LoginPage" in the logs
# -> put this code before __init__ below -> log = cl.custom_logger(logging.DEBUG)
from utilities import custom_logger as cl
import logging

from base.basepage import BasePage


# class LoginPage(SeleniumDriver): # inherit SeleniumDriver
class LoginPage(BasePage): # inherit BasePage -> which inherit SeleniumDriver

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver

    # Locators
    _email_field = "//input[@name='username']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[normalize-space()='Login']"
    _user_icon = "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']"
    _login_error_message = "//div[contains(@class, 'oxd-alert-content--error')]" # Invalid credentials



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
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()


    def verify_login_successful(self):
        result = self.is_element_present(self._user_icon)
        self.util.sleep(2)
        return result


    def verify_login_failed(self):
        result = self.get_text(self._login_error_message)
        return result


    def verify_login_error_message(self, expected_error_message):
        actual_error_message = self.get_text(self._login_error_message)
        print(f">>> actual_error_message = {actual_error_message}")
        print(f">>> expected_error_message = {expected_error_message}")
        self.util.sleep(2, "Waiting for the error message")
        if actual_error_message == expected_error_message:
            print("RETURN TRUE")
            return True
        else:
            print("RETURN FALSE")
            return False


    # def verify_login_failed2(self):
    #     result = self.get_text(self._login_error_message)
    #     assert result == "Invalid credentialss"

    # def verify_login_title(self):

    # def logout(self):


    def clear_fields(self):
        email_field = self.get_element(self._email_field)
        email_field.clear()
        password_field = self.get_element(self._password_field)
        password_field.clear()


    def verify_login_page_title(self):
        # time.sleep(2)
        # if self.get_title() == "OrangeHRM1":
        #     return True
        # else:
        #     return False
        return self.verify_page_title("OrangeHRM")


