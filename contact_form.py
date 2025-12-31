from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://inuberry.com/contact-us/"

NAME = "Test User"
EMAIL = "test@example.com"
MESSAGE = "Hello! This message was sent using Python Selenium automation."

driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 15)

name_input = wait.until(
    EC.presence_of_element_located((By.NAME, "form_fields[name]"))
)
email_input = wait.until(
    EC.presence_of_element_located((By.NAME, "form_fields[email]"))
)
message_input = wait.until(
    EC.presence_of_element_located((By.NAME, "form_fields[message]"))
)

name_input.send_keys(NAME)
email_input.send_keys(EMAIL)
message_input.send_keys(MESSAGE)

input("Solve CAPTCHA if present, then press Enter to submit...")

submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_btn.click()

print("Form submitted")

input("Press Enter to close browser...")
driver.quit()