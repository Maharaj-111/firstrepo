from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators for elements
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//span[contains(@class, 'error')]")
    dashboard_header = (By.XPATH, "//h1[text()='Dashboard']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message)).text

    def is_dashboard_displayed(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dashboard_header)).is_displayed()
