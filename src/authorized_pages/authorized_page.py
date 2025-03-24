from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import wait_for_element_to_be_visible


class AuthorizedPage:
    def __init__(self, driver: WebDriver) -> None:
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

    def _shopping_cart_link(self) -> WebElement:
        return self._primary_header().find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
        )

    def _secondary_header(self) -> WebElement:
        return self._header_container().find_element(
            By.CSS_SELECTOR, "div.header_secondary_container"
        )

    def _page_title(self) -> WebElement:
        return self._secondary_header().find_element(By.CSS_SELECTOR, "span.title")

    def _footer(self) -> WebElement:
        return self.root_element.find_element(By.CSS_SELECTOR, "footer.footer")

    def verify_user_has_logged_in_successfully(self) -> None:
        """
        Verify that the user has logged in successfully.

        Asserts:
            - The contents wrapper is displayed.
            - The footer is displayed.
        """
        assert self._contents_wrapper().is_displayed()
        assert self._footer().is_displayed()

    def verify_page_title(self, title: str) -> None:
        """
        Verify the page title.

        Args:
            title : str
                The expected title of the page.

        Asserts:
            - The page title matches the expected title.
        """
        wait_for_element_to_be_visible(self.driver, self._page_title())
        assert self._page_title().text == title
