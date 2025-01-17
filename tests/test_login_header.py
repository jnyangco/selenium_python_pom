import time

import allure
import pytest
# install "pytest-order" package
# pages
from pages.login_page import LoginPage
import utils.custom_logger as cl
from utils.util import Util
import logging

log = cl.custom_logger(logging.INFO)

# @pytest.mark.usefixtures("driver")
class TestLoginHeader:

    @allure.title("Login: Test Login Header")
    @pytest.mark.header
    def test_login_header(self, driver):
        login_page = LoginPage(driver)

        # Step 1: Validate header text are correct
        login_page.open_askomdch()
        expected_headers = ["Home", "Store", "Men", "Women", "Accessories", "Account", "About", "Contact Us"]
        login_page.verify_login_headers(expected_headers)
        time.sleep(2)


