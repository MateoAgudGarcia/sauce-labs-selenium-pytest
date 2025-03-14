from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class AuthorizedPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.root_element = self.driver.find_element(
            By.CSS_SELECTOR, "div#page_wrapper"
        )

    def _contents_wrapper(self) -> WebElement:
        return self.root_element.find_element(By.ID, "contents_wrapper")

    def _header_container(self) -> WebElement:
        return self.root_element.find_element(By.ID, "header_container")

    def _primary_header(self) -> WebElement:
        return self._header_container().find_element(
            By.CSS_SELECTOR, "div.primary_header"
        )

    def _secondary_header(self) -> WebElement:
        return self._header_container().find_element(
            By.CSS_SELECTOR, "div.header_secondary_container"
        )

    def _footer(self) -> WebElement:
        return self.root_element.find_element(By.CSS_SELECTOR, "footer.footer")

    def verify_user_has_logged_in_successfully(self):
        """
        Verify that the user has logged in successfully
        """
        assert self._contents_wrapper().is_displayed()
        assert self._footer().is_displayed()
