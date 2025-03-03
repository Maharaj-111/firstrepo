from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class PaymentModuleTest(unittest.TestCase):
    def setUp(self):
        """Initialize WebDriver"""
        self.driver = webdriver.Chrome()  # Use the correct path if needed
        self.driver.get("https://example.com/payment")  # Replace with actual URL
        self.driver.maximize_window()

    def test_valid_payment(self):
        """Test a successful payment with valid details"""
        driver = self.driver

        # Enter card number
        card_input = driver.find_element(By.ID, "cardNumber")
        card_input.send_keys("4111111111111111")  # Sample valid Visa test card

        # Enter expiration date
        exp_input = driver.find_element(By.ID, "expiryDate")
        exp_input.send_keys("12/26")

        # Enter CVV
        cvv_input = driver.find_element(By.ID, "cvv")
        cvv_input.send_keys("123")

        # Enter amount
        amount_input = driver.find_element(By.ID, "amount")
        amount_input.send_keys("100")

        # Submit payment
        submit_button = driver.find_element(By.ID, "payButton")
        submit_button.click()

        # Wait for response
        time.sleep(3)

        # Verify success message
        success_message = driver.find_element(By.ID, "paymentSuccess")
        self.assertTrue(success_message.is_displayed())

    def test_invalid_card_number(self):
        """Test payment with an invalid card number"""
        driver = self.driver

        card_input = driver.find_element(By.ID, "cardNumber")
        card_input.send_keys("123456")  # Invalid card

        exp_input = driver.find_element(By.ID, "expiryDate")
        exp_input.send_keys("12/26")

        cvv_input = driver.find_element(By.ID, "cvv")
        cvv_input.send_keys("123")

        amount_input = driver.find_element(By.ID, "amount")
        amount_input.send_keys("100")

        submit_button = driver.find_element(By.ID, "payButton")
        submit_button.click()

        time.sleep(3)

        error_message = driver.find_element(By.ID, "paymentError")
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        """Close browser after test"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
