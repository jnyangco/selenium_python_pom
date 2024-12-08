import allure
import pytest
# install "pytest-order" package
# pages
from pages.login_page import LoginPage
import utils.custom_logger as cl
from utils.util import Util
import logging

log = cl.custom_logger(logging.INFO)

@pytest.mark.usefixtures("setup")
class TestLoginHeader:

    @allure.title("Test Case: Test Login Header")
    @pytest.mark.header
    def test_login_header(self):
        login_page = LoginPage(self.driver)

        # Step 1: Validate header text are correct
        # Expected List = ["Home", "Store", "Men", "Women", "Accessories", "Account", "About", "Contact Us"]
        login_page.open_askomdch()
        login_page.verify_login_headers()
        login_page.header.click_header_store()


