import time
import unittest
from pages.login.login_page import LoginPage
import pytest
from utilities.report_status import ReportStatus
import utilities.custom_logger as cl
import logging
from ddt import ddt, data, unpack



@pytest.mark.usefixtures("onetime_setup", "set_up")
@ddt
class LoginFailedDataDriven(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.ts = ReportStatus(self.driver)


    @pytest.mark.order(1)
    # multiple data in Tuple format
    @data(("Admin1", "admin123", "Invalid credentials"),
          ("Admin2", "admin123", "Invalid credentials"),
          ("Admin3", "admin123", "Invalid credentials"))
    @unpack  # this will unpack the data/parameter below
    def test_invalid_login(self, username, password, error_message):
        # Step 1: Login using username and password
        self.lp.open_orangehrm()
        self.lp.login(username, password)

        # Step 2: Verify error message "Invalid credentials" is displayed
        result = self.lp.verify_login_error_message(error_message)
        self.ts.mark_final("test_invalid_login", result, "Error message verified")


