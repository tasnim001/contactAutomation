from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://inuberry.com/contact-us/"
#URL = "https://www.zendesk.com/contact/"

NAME = "John King"
EMAIL = "john2020@something.com"
MESSAGE = "Hello, this is john"

driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 15)

inputs = driver.find_elements(By.TAG_NAME, "input")
textareas = driver.find_elements(By.TAG_NAME, "textarea")

all_fields = inputs + textareas

def extract_attributes(el):
    return {
        "name": (el.get_attribute("name") or "").lower(),
        "id": (el.get_attribute("id") or "").lower(),
        "placeholder": (el.get_attribute("placeholder") or "").lower(),
        "aria": (el.get_attribute("aria-label") or "").lower(),
        "type": (el.get_attribute("type") or "").lower(),
        "element": el
    }

name_input = None
email_input = None
message_input = None

for field in all_fields:
    attrs = extract_attributes(field)
    combined = " ".join([
        attrs["name"],
        attrs["id"],
        attrs["placeholder"],
        attrs["aria"]
    ])
    if not email_input and ("email" in combined or attrs["type"] == "email"):
        email_input = attrs["element"]

    elif not message_input and field.tag_name.lower() == "textarea":
        message_input = attrs["element"]

    elif not message_input and (
        "message" in combined or "msg" in combined or "comment" in combined or "feedback" in combined
    ):
        message_input = attrs["element"]

    elif not name_input and ("name" in combined or "fullname" in combined):
        name_input = attrs["element"]


if name_input:
    name_input.send_keys(NAME)
if email_input:
    email_input.send_keys(EMAIL)
if message_input:
    message_input.send_keys(MESSAGE)

input("Solve CAPTCHA if present, then press Enter to submit...")

submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_btn.click()

print("Form submitted")

input("Press Enter to close browser...")
driver.quit()