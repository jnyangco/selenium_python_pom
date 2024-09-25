import time
import unittest
from selenium import webdriver
from pages.login.login_page import LoginPage
import pytest
# install pytest-order

@pytest.mark.usefixtures("onetime_setup", "set_up")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.lp = LoginPage(self.driver)


    @pytest.mark.order(2)
    def test_valid_login(self):
        # Step 1: Login using username and password
        self.lp.login("Admin", "admin123")

        # Step 2: User icon should be displayed
        result = self.lp.verify_login_successful()
        assert result == True

        time.sleep(2)


    @pytest.mark.order(1)
    def test_invalid_login(self):
        # Step 1: Login using username and password
        self.lp.login("Admin", "admin1234")

        # Step 2: Verify error message "Invalid credentials" is displayed
        result = self.lp.verify_login_failed()
        assert result == "Invalid credentials"

        time.sleep(2)


