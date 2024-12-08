import time
import allure
from selenium.webdriver.common.by import By
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

    # Locators
    _header_menu_account = (By.XPATH, "//li[@id='menu-item-1237']/a")
    _email_textbox = (By.XPATH, "//input[@id='username']")
    _password_textbox = (By.XPATH, "//input[@id='password']")
    _login_button = (By.XPATH, "//button[@value='Log in']")
    _login_hello_user_message = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p/strong[1]")

    _login_error_message = (By.XPATH, "//ul[@class='woocommerce-error']/li") # Invalid credentials
    _login_headers = (By.XPATH, "(//ul[@id='ast-hf-menu-1'])[1]/li")
    _header_store = (By.XPATH, "//li[@id='menu-item-1227']")


    @allure.step("Verify login headers are correct")
    def verify_login_headers(self):
        headers = self.get_element_list(self._login_headers)
        expected_headers = ["Home", "Store", "Men", "Women", "Accessories", "Account", "About", "Contact Uss"]

        try:
            assert len(headers) == len(expected_headers), \
                f">>> Failed: Expected total elements = {len(expected_headers)}, Actual total elements = {len(headers)}"
        except:
            self.report.mark(False, "Total header elements not matched")
            # self.screenshot(">>> Step Failed - taking screenshot...")

        try:
            for index, actual_header in enumerate(headers):
                assert actual_header.text == expected_headers[index], \
                    f"Header text mismatch at index {index}. Expected header = {expected_headers[index]}, Actual header = {actual_header.text}"
        except:
            self.report.mark_final("test_login_headers", False, "Header elements not matched")
            # self.screenshot(">>> Step Failed - taking screenshot...")


    # ACTION ---------------------------------------------------------------------------------------------------------
    def enter_username(self, email):
        # self.get_username_field().send_keys(email)
        self.send_text(email, self._email_textbox) # locator_type optional -> default value is xpath


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

    def open_orangehrm(self):
        # self.open_url("https://opensource-demo.orangehrmlive.com")
        # self.open_url("/admin")  # "/admin" is optional - positional arguments
        self.open_url()

    @allure.step("Open Askcomdch Website")
    def open_askomdch(self):
        # self.open_url("https://askomdch.com")
        # self.open_url("/admin")  # "/admin" is optional - positional arguments
        self.open_url()


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


