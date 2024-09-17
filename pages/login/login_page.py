from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        email_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        email_field.send_keys(username)

        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()

