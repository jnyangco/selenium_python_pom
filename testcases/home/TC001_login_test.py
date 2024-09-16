import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest:

    def test_valid_login(self):
        # base_url = "https://letskodeit.teachable.com"
        base_url = "https://opensource-demo.orangehrmlive.com"

        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        email_field = driver.find_element(By.XPATH, "//input[@name='username']")
        email_field.send_keys("Admin")

        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("admin123")
        # time.sleep(4)

        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()

        user_icon = driver.find_element(By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")
        if user_icon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        time.sleep(5)
        driver.quit()

test_case = LoginTest()
test_case.test_valid_login()
