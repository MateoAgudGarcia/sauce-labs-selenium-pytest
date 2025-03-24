from faker import Faker
from src.authorized_pages.overview_page import OverviewPage
from src.authorized_pages.authorized_page import AuthorizedPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import (
    wait_for_element_to_be_clickable,
    wait_for_element_to_be_visible,
)

faker = Faker()


class CheckoutPage(AuthorizedPage):
    def _checkout_info_container(self) -> WebElement:
        return self.root_element.find_element(By.ID, "checkout_info_container")

    def _checkout_info(self) -> WebElement:
        return self._checkout_info_container().find_element(
            By.CSS_SELECTOR, "div.checkout_info"
        )

    def _first_name(self) -> WebElement:
        return self._checkout_info().find_element(By.ID, "first-name")

    def _last_name(self) -> WebElement:
        return self._checkout_info().find_element(By.ID, "last-name")

    def _zip_code(self) -> WebElement:
        return self._checkout_info().find_element(By.ID, "postal-code")

    def _error_message(self) -> WebElement:
        return self._checkout_info().find_element(
            By.CSS_SELECTOR, "h3[data-test='error']"
        )

    def _checkout_buttons(self) -> WebElement:
        return self._checkout_info_container().find_element(
            By.CSS_SELECTOR, "div.checkout_buttons"
        )

    def _cancel_button(self) -> WebElement:
        return self._checkout_buttons().find_element(By.ID, "cancel")

    def _continue_button(self) -> WebElement:
        return self._checkout_buttons().find_element(By.ID, "continue")

    def fill_out_personal_information(self) -> None:
        """
        Define personal information with dummy values created by faker.
        """
        wait_for_element_to_be_visible(self.driver, self._checkout_info())
        self._first_name().send_keys(faker.first_name())
        self._last_name().send_keys(faker.last_name())
        self._zip_code().send_keys(faker.zipcode())

    def fill_out_with_empty_data(self) -> None:
        """
        Define wrong personal data with dummy values created by faker.
        """
        wait_for_element_to_be_visible(self.driver, self._checkout_info())
        self._first_name().send_keys(faker.first_name())
        self._zip_code().send_keys(faker.zipcode())
        wait_for_element_to_be_clickable(self.driver, self._continue_button())
        self._continue_button().click()
        assert "Error: " in self._error_message().text
        assert " is required" in self._error_message().text

    def go_to_overview(self) -> OverviewPage:
        """
        Go to the overview page.

        Returns:
            OverviewPage: An instance of the OverviewPage class.
        """
        wait_for_element_to_be_clickable(self.driver, self._continue_button())
        self._continue_button().click()
        return OverviewPage(self.driver)
