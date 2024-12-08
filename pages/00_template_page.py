import time
import allure
from selenium.webdriver.common.by import By

from pages.header import Header
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus


class StorePage(BasePage): # inherit BasePage -> which inherit SeleniumDriver

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver
        self.report = ReportStatus(self.driver)
        self.header = Header(self.driver)  # Reuse the Header class

    # Locators
    _header_menu_account = (By.XPATH, "//li[@id='menu-item-1237']/a")


    # ACTION ---------------------------------------------------------------------------------------------------------
    def enter_username(self, email):
        # self.get_username_field().send_keys(email)
        self.send_text(email, self._email_textbox) # locator_type optional -> default value is xpath


    def click_login_button(self):
        # self.get_login_button().click()
        self.element_click(self._login_button)





    # METHODS---------------------------------------------------------------------------------------------------------
    @allure.step("Login using username and password")
    def login(self, username, password):
        # self.driver.get("www.google.com")  # not working here
        # self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        time.sleep(2)
        self.click_login_button()


    def login_v2(self, username, password):
        self.send_text(username, self._email_textbox)
        self.send_text(password, self._password_textbox)
        time.sleep(2)
        self.element_click(self._login_button)


    @allure.step("Verify login error message")
    def verify_login_error_message(self, expected_error_message):
        actual_error_message = self.get_text(self._login_error_message)
        print(f">>> actual_error_message = {actual_error_message}")
        print(f">>> expected_error_message = {expected_error_message}")
        self.wait_seconds(2, "Waiting for the error message")

        # if actual_error_message == expected_error_message:
        #     print("RETURN TRUE")
        #     return True
        # else:
        #     print("RETURN FALSE")
        #     return False
        assert actual_error_message == expected_error_message, \
            f">>> Failed Step: actual_message = {actual_error_message}, expected_message = {expected_error_message}"


