'''The auth module contains functions that are related to authentication.'''
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


async def sign_in_to_codewars(
    driver: WebDriver, codewars_email: str, codewars_password: str
):
    """
    This function signs in to Codewars using a given email and password through a web driver.

    Args:
    - driver (WebDriver): WebDriver is an object that controls the web browser and allows the script
    to interact with it.
    - codewars_email (str): The email address associated with the Codewars account that you want to
    sign in to.
    - codewars_password (str): The password for the Codewars account that the user wants to sign in
    to.
    """
    try:
        driver.get("https://www.codewars.com/users/sign_in")
    except TimeoutError:
        print("The driver took too much time.")
        sys.exit(1)

    try:
        sign_in_form: WebElement = driver.find_element(By.ID, "new_user")
        driver.find_element(By.ID, "user_email").send_keys(codewars_email)
        driver.find_element(By.ID, "user_password").send_keys(codewars_password)
        sign_in_form.find_element(By.CSS_SELECTOR, 'button.is-red[type="submit"]').click()
    except NoSuchElementException:
        print("A web element was not found on the page (sign-in step).")
        sys.exit(1)
