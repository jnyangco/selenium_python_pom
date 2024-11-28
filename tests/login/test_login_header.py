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

@pytest.mark.usefixtures("setup")
class TestLoginHeader:

    @pytest.mark.smoke
    def test_login_header(self):
        login_page = LoginPage(self.driver)
        util = Util()

        # Step 1: Validate header text are correct
        # Expected List = ["Home", "Store", "Men", "Women", "Accessories", "Account", "About", "Contact Us"]
        login_page.open_askomdch()
        login_page.verify_login_headers()


