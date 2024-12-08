import time
import allure
from selenium.webdriver.common.by import By
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus
from pages.header import Header


class StorePage(BasePage): # inherit BasePage -> which inherit SeleniumDriver

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver
        self.report = ReportStatus(self.driver)
        self.header = Header(self.driver)

    # Locators
    _search_product_textbox = (By.XPATH, "//input[@id='woocommerce-product-search-field-0']")
    _search_button = (By.XPATH, "//button[text()='Search']")
    _add_to_cart_button_dynamic = "//h2[text()='{}']/following::a[text()='Add to cart'][1]"

    # _textbox_search_product = (By.XPATH, "")




    # ACTION ---------------------------------------------------------------------------------------------------------
    def enter_search_product(self, product):
        self.send_text(product, self._search_product_textbox)

    def click_search_button(self):
        self.element_click(self._search_button)

    def click_add_to_cart_dynamic(self, product):
        self.element_click((By.XPATH, self._add_to_cart_button_dynamic.format(product)))




    # METHODS---------------------------------------------------------------------------------------------------------
    @allure.step("Search product")
    def search_product(self, product):
        self.enter_search_product(product)
        self.click_search_button()

    @allure.step("Add to cart product")
    def add_to_cart_product(self, product):
        self.click_add_to_cart_dynamic(product)





