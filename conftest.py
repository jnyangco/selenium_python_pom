# conftest.py -> should be placed on testcase folder level
# ADDITIONAL INFO: conftest.py can be placed on the main project folder (not necessary to be inside the tests folder)
# Configuration Test -> common pytest method
import pytest
from selenium import webdriver
# from base.webdriverfactory import WebDriverFactory
# from pages.login.login_page import LoginPage

# BASIC SETUP ==================================
# @pytest.fixture(scope="function")
# def driver():
#     # Initialize the WebDriver
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#
#     yield driver
#
#     # Cleanup after test
#     driver.quit()


# ADVANCED SETUP ==================================
def pytest_addoption(parser):
    # Add CLI option for selecting the browser
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")


@pytest.fixture(scope="function")
def driver(request):
    # Get the browser type from the CLI option
    browser = request.config.getoption("--browser").lower()

    # Initialize the WebDriver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    # Cleanup after test
    driver.quit()





# PREVIOUS SETUP ==================================

# @pytest.fixture()
# def set_up(): # method level setup (default scope)
#     print("\n---------- Run before method (conftest.py) ----------")  # before method
#     yield
#     print("\nRun after method (conftest.py)")  # after method


# scope -> "module" (default), "class", "session" ... # module setup (i.e: Open browser > Quit browser)
# SCOPE:
# scope=session
# scope=package
# scope=module
# scope=class
# scope=function
#
# @pytest.fixture(scope="class") #


# ==================================================================
# actual usage
# --envi qa1 --browser chrome --report True --headless False
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--os_type", help="Type of operating system")
#
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture(scope="session")
# def os_type(request):
#     return request.config.getoption("--os_type")


