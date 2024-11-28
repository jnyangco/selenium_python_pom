import time
import unittest
import pytest
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.report_status import ReportStatus
import utils.custom_logger as cl
import logging
from ddt import ddt, data, unpack



@pytest.mark.usefixtures("setup", "method_setup")
@ddt
class LoginTestDataDriven(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    # @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.dp = DashboardPage(self.driver)
        self.ts = ReportStatus(self.driver)


    @pytest.mark.order(1)
    # multiple data in Tuple format
    @data(("Admin", "admin123"),
          ("Admin", "admin123"))
    @unpack  # this will unpack the data/parameter below
    def test_valid_login(self, username, password):
        # Step 1: Login using username and password
        self.lp.open_orangehrm()
        self.lp.login(username, password)

        # Step 2: Verify error message "Invalid credentials" is displayed
        result = self.dp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result, "Login verified")


