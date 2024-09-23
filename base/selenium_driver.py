from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# packages for logger
# import utilities.custom_logger
from utilities import custom_logger as cl
import logging


# Custom Class - wrapper for selenium webdriver
# Every Page Class -> should inherit from SeleniumDriver()
# i.e: LoginPage(SeleniumDriver)

class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        else:
            # print("Locator type " + locator_type + " is not supported.")
            self.log.info("Locator type " + locator_type + " is not supported.")
        return False


    # (LOCATOR, LOCATOR_TYPE)
    def get_element(self, locator, locator_type="xpath"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            # print("Element found with locator: " +locator + " and locator_type: " +locator_type)
            self.log.info("Element found with locator: " +locator + " and locator_type: " +locator_type)
        except:
            # print("Element not found with locator: " +locator + " and locator_type: " +locator_type)
            self.log.info("Element not found with locator: " +locator + " and locator_type: " +locator_type)
        return element


    def element_click(self, locator, locator_type="xpath"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            # print("Clicked on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Clicked on element with locator: " + locator + " locator Type: " + locator_type)
        except:
            # print("Cannot click on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot click on the element with locator: " + locator + " locator Type: " + locator_type)
            print_stack()


    def send_text(self, text, locator, locator_type="xpath"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(text)
            # print("Send text on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Send text on element with locator: " + locator + " locator Type: " + locator_type)
        except:
            # print("Cannot send text on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot send text on the element with locator: " + locator + " locator Type: " + locator_type)
            print_stack()


    def is_element_present(self, locator, locator_type="xpath"):
        try:
            # element = self.driver.find_element(by_type, locator)
            element = self.get_element(locator, locator_type)
            if element is not None:
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

    # check list of elements
    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
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


    def wait_for_element(self, locator, locator_type="xpath",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            # print("Waiting for maximum :: " + str(timeout) +
            #       " :: seconds for element to be clickable")
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type,
                                                             "stopFilter_stops-0")))
            # print("Element appeared on the web page")
            self.log.info("Element appeared on the web page")
        except:
            # print("Element not appeared on the web page")
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element





    def get_text(self, locator, locator_type="xpath"):
        try:
            element = self.get_element(locator, locator_type)
            text = element.text
            # print("Get text on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Get text on element with locator: " + locator + " locator Type: " + locator_type)
            return text
        except:
            # print("Cannot get text on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot get text on the element with locator: " + locator + " locator Type: " + locator_type)
            print_stack()