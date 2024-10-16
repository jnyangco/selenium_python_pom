import time
import unittest
from selenium import webdriver
from pages.login.login_page import LoginPage
import pytest
from utilities.report_status import ReportStatus
# install "pytest-order" package

import utilities.custom_logger as cl
import logging




@pytest.mark.usefixtures("onetime_setup", "set_up")
class LoginTest(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.ts = ReportStatus(self.driver)


    @pytest.mark.order(2)
    def test_valid_login(self):
        # Step 1: Login using username and password
        self.lp.login("Admin", "admin123")

        # Step 2: Verify page title is correct
        # result1 = self.lp.verify_page_title()
        # assert result1 == True
        result1 = self.lp.verify_login_page_title()  # result1 = True/False
        self.ts.mark(result1, "Title verified")

        # Step 3: User icon should be displayed
        # result2 = self.lp.verify_login_successful()
        # assert result2 == True
        result2 = self.lp.verify_login_successful()  # result2 = True/False
        time.sleep(2)
        self.ts.markFinal("test_valid_login", result2, "Login successful")




    # @pytest.mark.order(1)
    # def test_invalid_login(self):
    #     # Step 1: Login using username and password
    #     self.lp.login("Admin", "admin1234")
    #
    #     # Step 2: Verify error message "Invalid credentials" is displayed
    #     result = self.lp.verify_login_failed()
    #     assert result == "Invalid credentials"
    #
    #     time.sleep(2)


