import allure
import pytest
# install "pytest-order" package
# pages
from pages.login_page import LoginPage
import utils.custom_logger as cl
from utils.util import Util
import logging
from utils.config_reader import read_config as data

log = cl.custom_logger(logging.INFO)

# @pytest.mark.usefixtures("onetime_setup", "set_up")
# @pytest.mark.usefixtures("driver")
class TestLogin:


    @allure.title("Test Case: Test Valid Login")
    # @allure.description("This is to test the valid login functionality")
    @pytest.mark.login
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        util = Util()

        # Step 1: Login using valid username and password
        login_page.open_askomdch()
        # login_page.click_header_menu_account()
        login_page.header.click_header_account()
        username = data("credentials","username")
        password = data("credentials","password")
        login_page.login(username, password)

        # Step 2: Verify hello user message is correct
        login_page.verify_login_hello_user_message(username)
        # login_page.wait_seconds(4)


    @allure.title("Test Case: Test Invalid Login")
    # @allure.description("This is to test the invalid login functionality")
    @pytest.mark.login
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)

        # Step 1: Login using invalid username and password
        login_page.open_askomdch()
        # login_page.click_header_menu_account()
        login_page.header.click_header_account()
        username = data("credentials","username")
        invalid_password = "Password#387465"
        login_page.login(username, invalid_password)

        # Step 2: Verify error message is displayed
        login_page.verify_login_error_message("Error: The password you entered for the username {} is incorrect. "
                                              "Lost your password?".format(username))
