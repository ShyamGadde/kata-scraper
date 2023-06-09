import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


async def sign_in_to_codewars(driver, email, codewars_password):
    try:
        driver.get("https://www.codewars.com/users/sign_in")
    except TimeoutError:
        print("The driver took too much time.")
        sys.exit(1)

    email = "shyamgadde1602@gmail.com"
    codewars_password = "Q!2gxNAM^%M!U&"

    try:
        sign_in_form = driver.find_element(By.ID, "new_user")
        driver.find_element(By.ID, "user_email").send_keys(email)
        driver.find_element(By.ID, "user_password").send_keys(codewars_password)
        sign_in_form.find_element(By.CLASS_NAME, "is-red").click()
    except NoSuchElementException:
        print("A web element was not found on the page (sign-in step).")
        sys.exit(1)
