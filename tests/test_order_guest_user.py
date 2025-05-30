import time

import allure
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.store_page import StorePage
import utils.custom_logger as cl
from utils.util import Util
import logging
from utils.config_reader import read_config as data
log = cl.custom_logger(logging.INFO)

# @pytest.mark.usefixtures("driver")
class TestOrderGuestUser:

    @allure.title("Order: Test Order 'Blue Shoes' using Guest User")
    @pytest.mark.checkout
    def test_order_blue_shoes_guest_user(self, driver):
        login_page = LoginPage(driver)
        util = Util()

        # Step 1: Login using valid username and password
        login_page.open_askomdch()

        # Step 2: Click header store
        login_page.header.click_header_store()
        # login_page.wait_seconds(4)

        # Step 3: Search "shoes"
        store_page = StorePage(self.driver)
        store_page.search_product("shoes")

        # Step 4: Add to cart "Blue Shoes"
        store_page.add_to_cart_product("Blue Shoes")
        store_page.wait_seconds(2)

        # Step 5: Click cart in the header
        store_page.header.click_header_cart()

        # Step 6: Click [Proceed to Checkout] button
        cart_page = CartPage(self.driver)
        cart_page.click_proceed_to_checkout_button()
        # cart_page.wait_seconds(5)

        # Step 7: Verify user is redirected to Checkout page
        checkout_page = CheckoutPage(self.driver)
        checkout_page.verify_checkout_page()

        # Step 8: Fillup checkout page
        checkout_page.guest_fill_up_checkout_page("Fname", "Lname", "United States",
                                                  "123 Test Address", "Test City", "New York",
                                                  "12345", "guest_user1@test.com")
        checkout_page.wait_seconds(2)

        # Step 9: Click place order button
        checkout_page.click_place_order()
        checkout_page.wait_seconds(2)

        # Step 10: Verify order confirmation text
        checkout_page.verify_order_confirmation_text("Thank you. Your order has been received.")
        time.sleep(2)



