import unittest
import pytest
# install "pytest-order" package
# pages
from pages.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.report_status import ReportStatus
import utils.custom_logger as cl
import logging

log = cl.custom_logger(logging.INFO)

@pytest.mark.usefixtures("setup", "method_setup")
class TestTemplate(unittest.TestCase):

    @pytest.mark.order(1)
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        report = ReportStatus(self.driver)

        # Step 1: Login using username and password
        login_page.open_orangehrm()
        login_page.login("Admin", "admin123")

        # Step 2: Verify page title is correct
        result = login_page.verify_login_page_title()
        report.mark(result, "Title verified")

        # Step 3: User icon should be displayed
        result = dashboard_page.verify_login_successful()
        report.mark_final("test_valid_login", result, "Login successful")

