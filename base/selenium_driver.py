# this usually called "basepage"


import time

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# packages for logger
# import utils.custom_logger
from utils import custom_logger as cl
import logging

# for reports
import time
import os

from utils.config_reader import read_config


# Custom Class - wrapper for selenium webdriver
# Every Page Class -> should inherit from SeleniumDriver()
# i.e: LoginPage(SeleniumDriver)

class SeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)

    # like constructor
    def __init__(self, driver):
        self.driver = driver
        self.base_url = read_config("url", "base_url")


    # ===== METHODS BELOW ===== #
    # def open_url(self, base_url):
    #     self.driver.get(base_url)

    # positional argument -> by default it will open the base_url
    # if url is provided, it will open the provided url
    def open_url(self, url_path=""):
        url = self.base_url + url_path
        self.driver.get(url)

    def screenshot(self, result_message):
        """
        Takes the screenshot of the current open web
        """
        print()
        filename = result_message + "." + str(round(time.time() * 1000)) + ".png" #png is more compressed / smaller file
        screenshot_directory = "../reports/"
        relative_filename = screenshot_directory + filename  # this is the filepath

        current_directory = os.path.dirname(__file__)

        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            # if "reports" folder not exist, create a folder
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred ###")
            print_stack()


    def get_title(self):
        return self.driver.title

    # def get_by_type(self, locator_type):
    #     locator_type = locator_type.lower()
    #     if locator_type == "id":
    #         return By.ID
    #     elif locator_type == "name":
    #         return By.NAME
    #     elif locator_type == "class":
    #         return By.CLASS_NAME
    #     elif locator_type == "link":
    #         return By.LINK_TEXT
    #     elif locator_type == "css":
    #         return By.CSS_SELECTOR
    #     elif locator_type == "xpath":
    #         return By.XPATH
    #     else:
    #         # print("Locator type " + locator_type + " is not supported.")
    #         self.log.info("Locator type " + locator_type + " is not supported.")
    #     return False


    # (LOCATOR, LOCATOR_TYPE)
    # def get_element(self, locator, locator_type="xpath"):
    def get_element(self, locator):
        element = None
        try:
            # locator_type = locator_type.lower()
            # by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(*locator)
            # NOTE: * -> is used to unpack the locator values (By.ID, "button[@id='login']

            # print("Element found with locator: " +locator + " and locator_type: " +locator_type)

            # Temporary Commented Out
            # self.log.info("Element found with locator: " +str(locator))
        except:
            # print("Element not found with locator: " +locator + " and locator_type: " +locator_type)
            self.log.info("Element not found with locator: " +str(locator))
        return element


    def get_element_list(self, locator):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            # locator_type = locator_type.lower()
            # by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(*locator)
            self.log.info("Element list found with locator: " + str(locator))
        except:
            self.log.info("Element list not found with locator: " + str(locator))
        return element


    # def element_click(self, locator, locator_type="xpath"):
    def element_click(self, locator=""):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.get_element(locator)
            element.click()
            # print("Clicked on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Clicked on element with locator: " + str(locator))
        except:
            # print("Cannot click on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot click on the element with locator: " + str(locator))
            print_stack()


    # cannot use "send_keys" -> it is existing function
    # original from tutorial -> "sendKeys"
    # def send_text(self, text, locator, locator_type="xpath"):
    def send_text(self, text, locator=""):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.get_element(locator)
            element.send_keys(text)
            # print("Send text on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Send text on element with locator: " + str(locator))
        except:
            # print("Cannot send text on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot send text on the element with locator: " + str(locator))
            print_stack()


    # def get_text(self, locator, locator_type="xpath"):
    #     try:
    #         element = self.get_element(locator, locator_type)
    #         text = element.text
    #         # print("Get text on element with locator: " + locator + " locator Type: " + locator_type)
    #         self.log.info("Get text on element with locator: " + locator + " locator Type: " + locator_type)
    #         return text
    #     except:
    #         # print("Cannot get text on the element with locator: " + locator + " locator Type: " + locator_type)
    #         self.log.info("Cannot get text on the element with locator: " + locator + " locator Type: " + locator_type)
    #         print_stack()


    def get_text(self, locator="", info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            self.log.debug("In locator condition")
            element = self.get_element(locator)

            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))

            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    # def is_element_present(self, locator, locator_type="xpath"):
    def is_element_present(self, locator=""):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            # element = self.driver.find_element(by_type, locator)
            element = self.get_element(locator)
            if element is not None:
                # print("Element Found")
                # self.log.info("Element Found")
                self.log.info("Element present with locator: " + str(locator))
                return True
            else:
                # print("Element not found")
                # self.log.info("Element not found")
                self.log.info("Element NOT present with locator: " + str(locator))
                return False
        except:
            # print("Element not found")
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator=""):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            element = self.get_element(locator)
            if element is not None:
                is_displayed = element.is_displayed()  # is_displayed = True
                self.log.info("Element is displayed with locator: " + str(locator))
            else:
                self.log.info("Element not displayed with locator: " + str(locator))
            return is_displayed
        except:
            print("Element not found")
            return False


    # check list of elements
    def element_presence_check(self, locator):
        try:
            element_list = self.driver.find_elements(*locator)
            if len(element_list) > 0:
                # print("Element Found")
                self.log.info("Element Found")
                return True
            else:
                # print("Element not found")
                self.log.info("Element not found")
                return False
        except:
            # print("Element not found")
            self.log.info("Element not found")
            return False


    # RETURN ELEMENT
    def wait_for_element(self, locator, timeout=10, poll_frequency=0.5):
        element = None
        try:
            # by_type = self.get_by_type(locator_type)
            # print("Waiting for maximum :: " + str(timeout) +
            #       " :: seconds for element to be clickable")
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # element = wait.until(EC.element_to_be_clickable((locator, "stopFilter_stops-0"))) # not working
            # element = wait.until(EC.element_to_be_clickable(locator)) # this is also working
            element = wait.until(EC.visibility_of_element_located(locator))
            # print("Element appeared on the web page")
            self.log.info("Element appeared on the web page")
        except:
            # print("Element not appeared on the web page")
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def web_scroll(self, direction="down"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")