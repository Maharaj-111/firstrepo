from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the target page
driver.get('https://example.com')

# Locate the iframe using a CSS selector or XPath
iframe_element = driver.find_element(By.CSS_SELECTOR, 'iframe[class="iframe-class"]')
# Alternatively, using XPath
# iframe_element = driver.find_element(By.XPATH, '//iframe[contains(@class, "iframe-class")]')

# Switch to the located iframe
driver.switch_to.frame(iframe_element)

# Now you can interact with elements inside the iframe
# For example, find an element within the iframe
inner_element = driver.find_element(By.ID, 'element_inside_iframe')
inner_element.click()

# To exit the iframe and return to the main content
driver.switch_to.default_content()

