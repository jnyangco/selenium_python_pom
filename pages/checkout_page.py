import time
import allure
import pytest
from selenium.webdriver.common.by import By

from pages.header import Header
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus


class CheckoutPage(BasePage): # inherit BasePage -> which inherit SeleniumDriver

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver
        self.report = ReportStatus(self.driver)
        self.header = Header(self.driver)  # Reuse the Header class

    # Variables
    is_user_logged_in = False

    # Locators
    _checkout_header_label = (By.XPATH, "//h1[text()='Checkout']")
    _first_name_textbox = (By.XPATH, "//input[@id='billing_first_name']")
    _last_name_textbox = (By.XPATH, "//input[@id='billing_last_name']")
    _country_dropdown = (By.XPATH, "(//span[@aria-label='Country / Region'])[1]")
    _country_search_box = (By.XPATH, "//input[@class='select2-search__field']")
    _country_search_box_first_option = (By.XPATH, "//input[@class='select2-search__field']/following::span[1]")
    _street_address_textbox = (By.XPATH, "//input[@id='billing_address_1']")
    _city_textbox = (By.XPATH, "//input[@id='billing_city']")

    _state_dropdown = (By.XPATH, "//span[@id='select2-billing_state-container']")
    _state_search_box = (By.XPATH, "//input[@class='select2-search__field']")
    _state_search_box_first_option = (By.XPATH, "//input[@class='select2-search__field']/following::span[1]")
    # _department_dropdown = (By.XPATH, "//span[@id='select2-billing_state-container']")
    # _department_search_box = (By.XPATH, "//input[@class='select2-search__field']")
    # _department_search_box_first_option = (By.XPATH, "//input[@class='select2-search__field']/following::span[1]")
    _zip_code = (By.XPATH, "//input[@id='billing_postcode']")
    _email_address_textbox = (By.XPATH, "//input[@id='billing_email']")
    _place_order_button = (By.XPATH, "//button[@id='place_order']")

    _order_confirmation_text = (By.XPATH, "//div[@class='woocommerce-order']/p")



    # ACTION ---------------------------------------------------------------------------------------------------------
    @allure.step("Verify user is redirected to checkout page")
    def verify_checkout_page(self):
        self.is_element_displayed(self._checkout_header_label)

    @allure.step("Fill up checkout page")
    def guest_fill_up_checkout_page(self, first_name, last_name, country, street_address, city, state, zip_code, email_address=""):
        self.send_text(first_name, self._first_name_textbox)
        self.send_text(last_name, self._last_name_textbox)

        self.element_click(self._country_dropdown)
        time.sleep(1)
        self.send_text(country, self._country_search_box)
        time.sleep(1)
        self.element_click(self._country_search_box_first_option)
        time.sleep(1)

        self.send_text(street_address, self._street_address_textbox)
        self.send_text(city, self._city_textbox)

        # self.element_click(self._department_dropdown)
        # self.send_text(department, self._department_search_box)
        # self.element_click(self._department_search_box_first_option)

        self.element_click(self._state_dropdown)
        time.sleep(1)
        self.send_text(state, self._state_search_box)
        time.sleep(1)
        self.element_click(self._state_search_box_first_option)
        time.sleep(1)

        self.send_text(zip_code, self._zip_code)

        if email_address != "":
            self.send_text(email_address, self._email_address_textbox)

    @allure.step("Click place order button")
    def click_place_order(self):
        self.element_click(self._place_order_button)


    @allure.step("Verify order confirmation text")
    def verify_order_confirmation_text(self, expected_text):
        actual_text = self.get_text(self._order_confirmation_text)
        assert actual_text == expected_text, pytest.fail(f"FAILED: Incorrect order confirmation text."
                                                         f"Expected = {expected_text}, Actual = {actual_text}")





    # METHODS---------------------------------------------------------------------------------------------------------



