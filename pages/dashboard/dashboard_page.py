
from utilities import custom_logger as cl
import logging
from base.basepage import BasePage


class DashboardPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # calling __init__ method of superclass (SeleniumDriver/BasePage???) and providing the driver
        self.driver = driver


    # Locators
    _search_textbox = "//input[@placeholder='Search']"
    _first_menu_result = "//div[@class='oxd-sidepanel-body']/ul[1]"
    _add_button = "//button[normalize-space()='Add']"
    _user_icon = "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']"
    _logout_option = "//a[text()='Logout']"


    # ACTION ---------------------------------------------------------------------------------------------------------
    def enter_search_text(self, search_text):
        self.send_text(search_text, self._search_textbox)

    def click_first_menu_result(self):
        self.element_click(self._first_menu_result)

    def click_user_icon(self):
        self.element_click(self._user_icon)

    def click_logout_option(self):
        self.element_click(self._logout_option)


    # METHODS---------------------------------------------------------------------------------------------------------
    def search_menu(self, search_text):
        self.enter_search_text(search_text)
        self.util.wait(4)
        self.click_first_menu_result()
        self.util.wait(4)


    def verify_login_successful(self):
        result = self.is_element_present(self._user_icon)
        self.util.wait(2)
        return result


    def logout(self):
        self.click_user_icon()
        self.util.wait(2)
        self.click_logout_option()

