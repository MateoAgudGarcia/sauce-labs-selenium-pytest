import os
import allure

from dotenv import load_dotenv
from src.login.login_page import LoginPage

load_dotenv()

STANDARD_USER = os.getenv("STANDARD_USER")
LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER")
INVALID_USER = f"{None}"
PASSWORD = os.getenv("PASSWORD")


@allure.parent_suite("Sauce Labs - Demo")
@allure.suite("User with valid credentials")
@allure.title(
    "Choose the second most expensive product,"
    + " add it to the cart, and complete the order"
)
def test_completed_order(driver):
    with allure.step("Open the login page"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        login_page = LoginPage(driver)
        login_page.login(STANDARD_USER, PASSWORD)

    with allure.step("User has been logged in successfully"):
        inventory_page = login_page.access_to_inventory()
        inventory_page.verify_user_has_logged_in_successfully()

    with allure.step("Sort products by price (high to low)"):
        inventory_page.verify_page_title("Products")
        inventory_page.select_product_sort("Price (high to low)")

    with allure.step("Open the product details to the second product"):
        product_details_page = inventory_page.open_product_details(1)

    with allure.step("Verify that the product price is $29.99"):
        product_details_page.verify_product_price("$29.99")

    with allure.step("Add the product to the cart"):
        product_details_page.add_product_to_cart()

    with allure.step("Go to shopping cart"):
        shopping_cart_page = product_details_page.go_to_shopping_cart()
        shopping_cart_page.verify_page_title("Your Cart")
        shopping_cart_page.verify_quantity_by_product_index(0, 1)
        shopping_cart_page.verify_price_by_product_index(0, "$29.99")

    with allure.step("Go to checkout"):
        checkout_page = shopping_cart_page.go_to_checkout()
        checkout_page.verify_page_title("Checkout: Your Information")

    with allure.step("Fill out personal information"):
        checkout_page.fill_out_personal_information()

    with allure.step("Go to overview"):
        overview_page = checkout_page.go_to_overview()
        overview_page.verify_page_title("Checkout: Overview")

    with allure.step("Complete the order"):
        complete_order_page = overview_page.go_to_completed_order()
        complete_order_page.verify_page_title("Checkout: Complete!")
        complete_order_page.verify_checkout_is_completed()


@allure.parent_suite("Sauce Labs - Demo")
@allure.suite("User with valid credentials")
@allure.title("Choose a product, add it to the cart, and set a wrong personal data")
def test_wrong_shipping_information(driver):
    with allure.step("Open the login page"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        login_page = LoginPage(driver)
        login_page.login(STANDARD_USER, PASSWORD)

    with allure.step("User has been logged in successfully"):
        inventory_page = login_page.access_to_inventory()
        inventory_page.verify_user_has_logged_in_successfully()

    with allure.step("Sort products by name (z to a)"):
        inventory_page.verify_page_title("Products")
        inventory_page.select_product_sort("Name (Z to A)")

    with allure.step("Open the product details to the third product"):
        product_details_page = inventory_page.open_product_details(2)

    with allure.step("Verify that the product price is $49.99"):
        product_details_page.verify_product_price("$49.99")

    with allure.step("Add the product to the cart"):
        product_details_page.add_product_to_cart()

    with allure.step("Go to shopping cart"):
        shopping_cart_page = product_details_page.go_to_shopping_cart()
        shopping_cart_page.verify_page_title("Your Cart")
        shopping_cart_page.verify_quantity_by_product_index(0, 1)
        shopping_cart_page.verify_price_by_product_index(0, "$49.99")

    with allure.step("Go to checkout"):
        checkout_page = shopping_cart_page.go_to_checkout()
        checkout_page.verify_page_title("Checkout: Your Information")

    with allure.step("Fill out with wrong personal data"):
        checkout_page.fill_out_with_empty_data()


@allure.parent_suite("Sauce Labs - Demo")
@allure.suite("User with wrong credentials")
@allure.title("Try to login with a locked out user")
def test_with_a_locked_out_user(driver):
    with allure.step("Open the login page"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with a locked user credentials"):
        login_page = LoginPage(driver)
        login_page.login(LOCKED_OUT_USER, PASSWORD)


@allure.parent_suite("Sauce Labs - Demo")
@allure.suite("User with wrong credentials")
@allure.title("Try to login with an invalid user")
def test_with_an_invalid_user(driver):
    with allure.step("Open the login page"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with an invalid user credentials"):
        login_page = LoginPage(driver)
        login_page.login(INVALID_USER, PASSWORD)
