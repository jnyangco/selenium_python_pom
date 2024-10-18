import time
import unittest
from selenium import webdriver
import pytest

# pages
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utilities.report_status import ReportStatus
# install "pytest-order" package

import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("onetime_setup", "set_up")
class LoginAndLogout(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.dp = DashboardPage(self.driver)
        self.ts = ReportStatus(self.driver)


    @pytest.mark.order(1)
    def test_login_and_logout(self):
        # Step 1: Login using username and password
        self.lp.open_orangehrm()
        self.lp.login("Admin", "admin123")

        # Step 2: Verify page title is correct
        result = self.lp.verify_login_page_title()  # result1 = True/False
        self.ts.mark(result, "Title verified")

        # Step 3: User icon should be displayed
        result = self.dp.verify_login_successful()  # result2 = True/False
        time.sleep(2)
        self.ts.mark(result, "Login successful")

        # Step 4: Logout
        self.dp.logout()
        result = self.lp.verify_user_is_logged_out()
        self.ts.mark_final("test_valid_login_and_logout", result, "Login and logout successful")

