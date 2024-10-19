import time
import unittest
from selenium import webdriver
import pytest
# install "pytest-order" package

# pages
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utilities.report_status import ReportStatus

import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("onetime_setup", "set_up")
class LoginTest(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.dp = DashboardPage(self.driver)
        self.ts = ReportStatus(self.driver)

    # method override
    # def setUp(self):
    #     print('test')

    # NOTE: function should start with "test"
    @pytest.mark.order(1)
    def test_valid_login(self):
        # Step 1: Login using username and password
        self.lp.open_orangehrm()
        self.lp.login("Admin", "admin123")


        # Step 2: Verify page title is correct
        # result1 = self.lp.verify_page_title()
        # assert result1 == True
        result = self.lp.verify_login_page_title()  # result1 = True/False
        self.ts.mark(result, "Title verified")


        # Step 3: User icon should be displayed
        # result2 = self.lp.verify_login_successful()
        # assert result2 == True
        result = self.dp.verify_login_successful()  # result2 = True/False
        self.ts.mark_final("test_valid_login", result, "Login successful")


