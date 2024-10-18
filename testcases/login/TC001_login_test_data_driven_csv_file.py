import time
import unittest
from pages.login.login_page import LoginPage
import pytest
from utilities.report_status import ReportStatus
import utilities.custom_logger as cl
import logging
from ddt import ddt, data, unpack
from utilities.read_data import read_csv_data


@pytest.mark.usefixtures("onetime_setup", "set_up")
@ddt
class LoginTestDataDrivenCSVFile(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.ts = ReportStatus(self.driver)


    @pytest.mark.order(1)
    # multiple data in Tuple format
    # * -> telling python there are multiple arguments, need to unpack multiple data in a list
    @data(*read_csv_data("/Users/jerome/Documents/Code/Selenium Python/selenium_python_pom/testdata_login.csv"))
    @unpack  # this will unpack the data/parameter below
    def test_valid_login(self, username, password):
        # Step 1: Login using username and password
        self.lp.login(username, password)

        # Step 2: Verify error message "Invalid credentials" is displayed
        result = self.lp.verify_login_successful()
        self.ts.markFinal("test_valid_login", result, "Login verified")


