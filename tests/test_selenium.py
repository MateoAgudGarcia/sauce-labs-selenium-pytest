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

    with allure.step("User has been logged in successfully"):
        inventory_page = login_page.access_to_inventory()
        inventory_page.verify_user_has_logged_in_successfully()

    with allure.step("Sort products by price (high to low)"):
        inventory_page.select_product_sort("Price (high to low)")

    with allure.step("Open the product details to the second product"):
        product_details_page = inventory_page.open_product_details(1)

    with allure.step("Verify that the product price is $29.99"):
        product_details_page.verify_product_price("$29.99")
