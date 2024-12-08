import allure
import pytest
from pages.login_page import LoginPage
import utils.custom_logger as cl
from utils.util import Util
import logging
from utils.config_reader import read_config as data
log = cl.custom_logger(logging.INFO)

@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("Test Case: Test Order Product")
    @pytest.mark.order
    def test_order_product(self):
        login_page = LoginPage(self.driver)
        util = Util()

        # Step 1: Login using valid username and password
        login_page.open_askomdch()
        login_page.header.click_header_account()
        username = data("credentials","username")
        password = data("credentials","password")
        login_page.login(username, password)

        # Step 2: Click header store
        login_page.header.click_header_store()
        login_page.header.click_header_store()
        login_page.wait_seconds(10)

