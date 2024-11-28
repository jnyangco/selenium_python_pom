import time
import unittest
from selenium import webdriver
import pytest
# install "pytest-order" package
# pages
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.report_status import ReportStatus
import utils.custom_logger as cl
from utils.util import Util
import logging
from utils.config_reader import read_config as data

log = cl.custom_logger(logging.INFO)

@pytest.mark.usefixtures("onetime_setup", "set_up")
class TestLogin:

    @pytest.mark.login
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        util = Util()

        # Step 1: Login using valid username and password
        login_page.open_askomdch()
        login_page.click_header_menu_account()
        username = data("credentials","username")
        password = data("credentials","password")
        login_page.login(username, password)
        util.wait(10)

        # Step 2: Verify hello user message is correct
        login_page.verify_login_hello_user_message(username)


    def test_invalid_login(self):
        login_page = LoginPage(self.driver)

        # Step 1: Login using invalid username and password
        login_page.open_askomdch()
        login_page.click_header_menu_account()
        username = data("credentials","username")
        invalid_password = "Password#387465"
        login_page.login(username, invalid_password)

        # Step 2: Verify error message is displayed
        login_page.verify_login_error_message("Error: The password you entered for the username {} is incorrect. "
                                              "Lost your password?".format(username))
