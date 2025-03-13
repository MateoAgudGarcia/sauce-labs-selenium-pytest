from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import wait_for_element_to_be_clickable


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.root_element = self.driver.find_element(
            By.CSS_SELECTOR, ".login_container"
        )

    def login_wrapper(self) -> WebElement:
        return self.root_element.find_element(By.ID, "login_button_container")

    def username_input(self) -> WebElement:
        return self.login_wrapper().find_element(By.ID, "user-name")

    def password_input(self) -> WebElement:
        return self.login_wrapper().find_element(By.ID, "password")

    def login_button(self) -> WebElement:
        return self.login_wrapper().find_element(By.CSS_SELECTOR, "input#login-button")

    def login(self, username: str, password: str):
        self.username_input().send_keys(username)
        self.password_input().send_keys(password)

        login_button = wait_for_element_to_be_clickable(self.driver, self.login_button())
        login_button.click()
