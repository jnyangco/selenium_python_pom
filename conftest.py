# conftest.py -> should be placed on testcase folder level
# ADDITIONAL INFO: conftest.py can be placed on the main project folder (not necessary to be inside the tests folder)
# Configuration Test -> common pytest method
import pytest
from selenium import webdriver
from base.driver_factory import DriverFactory
# from pages.login.login_page import LoginPage

@pytest.fixture()
def method_setup(): # method level setup (default scope)
    print("\n---------- Run before method (conftest.py) ----------")  # before method
    yield
    print("\nRun after method (conftest.py)")  # after method


# actual usage
# --envi qa1 --browser chrome --report True --headless False
def pytest_addoption(parser):
    """Add CLI option for selecting the browser."""
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser to use")
    parser.addoption("--os_type", action="store", default="", help="Type of operating system")



# scope -> "module" (default), "class", "session" ... # module setup (i.e: Open browser > Quit browser)
# SCOPE:
# scope=session
# scope=package
# scope=module = python file
# scope=class
# scope=function
#
# @pytest.fixture(scope="class") # default from tutorial
# @pytest.fixture(scope="function") # when each test in a single python file need to reset setup (i.e: opening browser)
@pytest.fixture(scope="function")
def setup(request):  # --browser from command line
    print("\n========== Run one time setup (conftest.py) ==========")  # before method

    """Fixture to initialize and quit WebDriver."""
    browser = request.config.getoption("--browser").lower()
    os_type = request.config.getoption("--os_type").lower()

    print(f">>> BROWSER = {browser}")

    # Get Driver Instance
    driver_factory = DriverFactory(browser)
    driver = driver_factory.get_driver_instance()

    # Setting Driver Implicit Time out for An Element
    driver.implicitly_wait(10)

    # Maximize the window
    driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver  # Attach driver to the test class -> i.e: TestLogin: (CLASS)
    """
    USAGE: This code snippet appears to be part of a Python testing framework setup, possibly using pytest. It seems to be setting up a class-level fixture for tests that require a driver object, commonly used in automated browser testing frameworks like Selenium.
    Here's an explanation of the code:

    Context
	•	request: This is a built-in pytest fixture that provides information about the requesting test function or class.
	•	request.cls: Refers to the test class in which the test is being executed. If None, it indicates that the test is not part of a class.
	•	driver: Likely represents a WebDriver instance (e.g., Selenium WebDriver for automating browsers).
	
	Purpose: If the test is part of a class (request.cls is not None), it assigns the driver instance to the driver attribute of the test class.
	This makes the driver accessible to all methods within that test class.
    """

    yield driver  # yield + return driver instance for (Test Classes and Page Classes)


    print("\n========== Run one time teardown (conftest.py) ==========")  # after method
    driver.quit() # Teardown: Close the driver after tests


# ==================================================================






