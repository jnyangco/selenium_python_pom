import time
import unittest
import pytest
# pages
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.report_status import ReportStatus
# install "pytest-order" package
import utils.custom_logger as cl
import logging

log = cl.custom_logger(logging.INFO)

@pytest.mark.usefixtures("setup", "method_setup")
class TestDashboardUIVerification(unittest.TestCase):

    # @pytest.mark.order(1)
    def test_dashboard_header_verification(self):
        print(f"Test Case: {__name__}")
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        report = ReportStatus(self.driver)

        # Step 1: Login using username and password
        login_page.open_orangehrm()
        login_page.login("Admin", "admin123")
        result = dashboard_page.verify_login_successful()
        report.mark(result, "Login successful")

        # Step 2: Validate the following elements are showing up in the header
        result = dashboard_page.verify_header_elements_displayed()
        report.mark_final("test_dashboard_header_verification", result, "Header elements are displayed")






