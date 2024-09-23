import time
import unittest
from selenium import webdriver
from pages.login.login_page import LoginPage
import pytest

class LoginTest(unittest.TestCase):
    base_url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)


    @pytest.mark.run(order=2)
    def test_valid_login(self):
        # Step 1: Go to url https://opensource-demo.orangehrmlive.com
        self.driver.get(self.base_url)

        # Step 2: Login using username and password
        lp = LoginPage(self.driver)
        lp.login("Admin", "admin123")

        # Step 3: User icon should be displayed
        result = lp.verify_login_successful()
        assert result == True

        # Step 4: Close the browser
        time.sleep(2)
        self.driver.quit()


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        # Step 1: Go to url https://opensource-demo.orangehrmlive.com
        self.driver.get(self.base_url)

        # Step 2: Login - invalid password
        lp = LoginPage(self.driver)
        lp.login("Admin", "admin1234")

        # Step 3: Verify error message "Invalid credentials" is displayed
        result = lp.verify_login_failed()
        assert result == "Invalid credentials"

        # Step 4: Close the browser
        time.sleep(2)
        # self.driver.quit()


