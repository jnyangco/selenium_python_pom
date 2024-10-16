import time
import unittest
from selenium import webdriver
from pages.login.login_page import LoginPage
import pytest
from utilities.report_status import ReportStatus
# install "pytest-order" package

import utilities.custom_logger as cl
import logging

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.usefixtures("onetime_setup", "set_up")
class DashboardTest(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.dp = DashboardPage(self.driver)
        self.ts = ReportStatus(self.driver)

    @pytest.mark.order(1)
    def test_search_dashboard_menu(self):

        # Step 1: Login using username and password
        self.lp.login("Admin", "admin123")
        time.sleep(5)

        # Step 2: Search menu from dashboard then click the first result
        self.dp.search_menu("PIM")


        # Step 3:
        # check user is redirected to url https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList




