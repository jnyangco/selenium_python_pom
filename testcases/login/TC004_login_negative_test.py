import time
import unittest
import pytest
# pages
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utilities.report_status import ReportStatus
# install "pytest-order" package
import utilities.custom_logger as cl
import logging
log = cl.custom_logger(logging.INFO)


@pytest.mark.usefixtures("onetime_setup", "set_up")
class LoginNegativeTest(unittest.TestCase):

    @pytest.mark.order(1)
    def test_login_negative(self):
        login_page = LoginPage(self.driver)
        report = ReportStatus(self.driver)

        # Step 1: Login using username and password
        login_page.open_orangehrm()
        login_page.login("AdminTest", "admin123")

        # Step 2: Verify error message is displayed
        result = login_page.verify_login_error_message("Invalid credentials")
        report.mark_final("test_invalid_login", result, "Error message verified")
