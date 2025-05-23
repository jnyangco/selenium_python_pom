import unittest
from pages.login_page import LoginPage
import pytest
from utils.report_status import ReportStatus
from pages.dashboard.dashboard_page import DashboardPage
import utils.custom_logger as cl
import logging
from ddt import ddt, data, unpack
from utils.read_data import read_csv_data


@pytest.mark.usefixtures("driver", "method_setup")
@ddt
class LoginTestDataDrivenCSVFile(unittest.TestCase):

    log = cl.custom_logger(logging.INFO)

    # @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)
        self.dp = DashboardPage(self.driver)
        self.ts = ReportStatus(self.driver)


    @pytest.mark.order(1)
    # multiple data in Tuple format
    # * -> telling python there are multiple arguments, need to unpack multiple data in a list
    @data(*read_csv_data("/testdata_login.csv"))
    @unpack  # this will unpack the data/parameter below
    def test_valid_login(self, username, password):
        # Step 1: Login using username and password
        self.lp.open_orangehrm()
        self.lp.login(username, password)

        # Step 2: Verify error message "Invalid credentials" is displayed
        result = self.dp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result, "Login verified")


