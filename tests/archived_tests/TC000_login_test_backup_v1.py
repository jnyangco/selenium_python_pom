import time
import unittest

from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage

class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        # base_url = "https://letskodeit.teachable.com"
        base_url = "https://opensource-demo.orangehrmlive.com"
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.implicitly_wait(5)



        # Step 1: Go to url https://opensource-demo.orangehrmlive.com
        driver.get(base_url)

        # Step 2: Login using username and password
        lp = LoginPage(driver)
        lp.login("Admin", "admin123")

        # Step 3: User icon should be displayed
        dp = DashboardPage
        result = dp.verify_login_successful()
        assert result == True


        # Step: Close the browser
        time.sleep(2)
        driver.quit()


# to run LoginTest::test_valid_login -> no need to use this when using unittest
# test_case = LoginTest()
# test_case.test_valid_login()
