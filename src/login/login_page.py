from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from src.authorized_pages.inventory_page import InventoryPage
from utilities.utils import wait_for_element_to_be_clickable


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.root_element = self.driver.find_element(
            By.CSS_SELECTOR, ".login_container"
        )

    def _login_wrapper(self) -> WebElement:
        return self.root_element.find_element(By.ID, "login_button_container")

    def _username_input(self) -> WebElement:
        return self._login_wrapper().find_element(By.ID, "user-name")

    def _password_input(self) -> WebElement:
        return self._login_wrapper().find_element(By.ID, "password")

    def _login_button(self) -> WebElement:
        return self._login_wrapper().find_element(By.CSS_SELECTOR, "input#login-button")

    def login(self, username: str, password: str):
        """
        Login with the provided username and password
        """
        self._username_input().send_keys(username)
        self._password_input().send_keys(password)

        login_button = wait_for_element_to_be_clickable(
            self.driver, self._login_button()
        )
        login_button.click()

    def access_to_inventory(self) -> InventoryPage:
        """
        Access to inventory page
        """
        return InventoryPage(self.driver)
