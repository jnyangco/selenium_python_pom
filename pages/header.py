import time
import allure
from selenium.webdriver.common.by import By
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus

class Header(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver
        self.report = ReportStatus(self.driver)


    # Locators for header elements
    # _login_headers = (By.XPATH, "(//ul[@id='ast-hf-menu-1'])[1]/li")
    _header_account = (By.XPATH, "//li[@id='menu-item-1237']/a")
    _header_store = (By.XPATH, "//li[@id='menu-item-1227']")


    # Actions for the header elements
    @allure.step("Click Account menu in the header")
    def click_header_account(self):
        self.element_click(self._header_account)


    @allure.step("Click Store menu in the header")
    def click_header_store(self):
        self.element_click(self._header_store)



