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

log = cl.custom_logger(logging.INFO)


@pytest.mark.usefixtures("onetime_setup", "set_up")
class TestLogin:


    # @pytest.mark.order(1)
    @pytest.mark.login
    def test_valid_login1(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        report = ReportStatus(self.driver)

        # Step 1: Login using username and password
        login_page.open_orangehrm()
        login_page.login("Admin", "admin123")
        # login_page.login_v2("Admin", "admin123")

        # Step 2: Verify page title is correct
        result = login_page.verify_login_page_title()
        # result = login_page.verify_login_page_title_v2()
        report.mark(result, "Title verified")

        # Step 3: User icon should be displayed
        result = dashboard_page.verify_login_successful()
        # result = dashboard_page.verify_login_successful_v2()
        report.mark_final("test_valid_login", result, "Login successful")

