import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login.login_page import LoginPage

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

        # Step 3: 

        user_icon = driver.find_element(By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")
        if user_icon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        time.sleep(2)
        driver.quit()


# to run LoginTest::test_valid_login -> no need to use this when using unittest
# test_case = LoginTest()
# test_case.test_valid_login()
