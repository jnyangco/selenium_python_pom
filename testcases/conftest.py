# Configuration Test -> common pytest method
import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
# from pages.login.login_page import LoginPage

@pytest.fixture()
def set_up(): # method level setup (default scope)
    print("\n---------- Run before method (conftest.py) ----------")  # before method
    yield
    print("\nRun after method (conftest.py)")  # after method


# scope -> "module" (default), "class", "session" ... # module setup (i.e: Open browser > Quit browser)
@pytest.fixture(scope="class")
def onetime_setup(request, browser, os_type): # --browser from command line
    print("\n========== Run one time setup (conftest.py) ==========")  # before method

    # Get Driver Instance
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    # include login to application by default
    # lp = LoginPage(driver)
    # lp.login("test@email.com", "abc")

    # if browser.lower() == "firefox":
    #     base_url = "https://opensource-demo.orangehrmlive.com"
    #     driver = webdriver.Firefox()
    #     driver.implicitly_wait(5)
    #     driver.get(base_url)
    #     print(">>> Browser = Firefox")
    # else:
    #     base_url = "https://opensource-demo.orangehrmlive.com"
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(5)
    #     driver.get(base_url)
    #     print(">>> Browser = Chrome")

    if request.cls is not None:
        request.cls.driver = driver  # add value to class attribute

    yield driver  # yield + return driver instance for (Test Classes and Page Classes)

    print("\n========== Run one time teardown (conftest.py) ==========")  # after method
    driver.quit()


# ==================================================================
# actual usage
# --envi qa1 --browser chrome --report True --headless False
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")


