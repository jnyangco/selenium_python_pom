import time
import allure
from selenium.webdriver.common.by import By

from pages.header import Header
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus


class CartPage(BasePage): # inherit BasePage -> which inherit SeleniumDriver

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver
        self.report = ReportStatus(self.driver)
        self.header = Header(self.driver)  # Reuse the Header class

    # Locators
    _proceed_to_checkout_button = (By.XPATH, "//div[@class='wc-proceed-to-checkout']/a")



    # ACTION ---------------------------------------------------------------------------------------------------------
    @allure.step("Click proceed to checkout button")
    def click_proceed_to_checkout_button(self):
        self.element_click(self._proceed_to_checkout_button)






    # METHODS---------------------------------------------------------------------------------------------------------



