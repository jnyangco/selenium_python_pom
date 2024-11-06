from selenium.webdriver.common.by import By
from utilities import custom_logger as cl
import logging
from base.basepage import BasePage


class DashboardPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver


    # Locators
    _search_textbox = (By.XPATH, "//input[@placeholder='Search']")
    _first_menu_result = (By.XPATH, "//div[@class='oxd-sidepanel-body']/ul[1]")
    _add_button = (By.XPATH, "//button[normalize-space()='Add']")
    _logout_option = (By.XPATH, "//a[text()='Logout']")

    _header_dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")
    _header_upgrade_button = (By.XPATH, "//button[text()=' Upgrade']")
    _header_user_icon = (By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")


    # ACTION ---------------------------------------------------------------------------------------------------------
    def enter_search_text(self, search_text):
        self.send_text(search_text, self._search_textbox)

    def click_first_menu_result(self):
        self.element_click(self._first_menu_result)

    def click_user_icon(self):
        self.element_click(self._header_user_icon)

    def click_logout_option(self):
        self.element_click(self._logout_option)


    # METHODS---------------------------------------------------------------------------------------------------------
    def search_menu(self, search_text):
        self.enter_search_text(search_text)
        self.util.wait(2)
        self.click_first_menu_result()
        self.util.wait(2)


    def verify_login_successful(self):
        result = self.is_element_present(self._header_user_icon)
        self.util.wait(2)
        return result


    def logout(self):
        self.click_user_icon()
        self.util.wait(1)
        self.click_logout_option()


    def verify_header_elements_displayed(self):
        bool_list = []
        result = self.is_element_present(self._header_dashboard_text)
        bool_list.append(result)
        print(f'Result -> _header_dashboard_text = {result}')

        result = self.is_element_present(self._header_upgrade_button)
        bool_list.append(result)
        print(f'Result -> _header_upgrade_button = {result}')

        result = self.is_element_present(self._header_user_icon)
        bool_list.append(result)
        print(f'Result -> _header_user_icon = {result}')

        result = all(bool_list)
        print(f'Result -> verify_header_elements_displayed = {result}')

        return result


