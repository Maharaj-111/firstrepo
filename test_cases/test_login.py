import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.excel_reader import read_test_data

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")  # Replace with the actual URL
    yield driver
    driver.quit()

test_data_from_excel = read_test_data()

@pytest.mark.parametrize("data", test_data_from_excel)
def test_login(driver, data):
    login_page = LoginPage(driver)
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    if data["expected"] == "Login Successful":
        assert "Dashboard" in driver.title
    else:
        assert login_page.get_error_message() == data["expected"]
