import os
import allure

from dotenv import load_dotenv
from src.login.login_page import LoginPage

load_dotenv()


@allure.parent_suite("Sauce Labs - Demo")
@allure.suite("Login")
@allure.title("User can login with valid credentials")
def test_login_success(driver):
    standard_user = os.getenv("STANDARD_USER")
    password = os.getenv("PASSWORD")

    with allure.step("Open the login page"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        login_page = LoginPage(driver)
        login_page.login(standard_user, password)
