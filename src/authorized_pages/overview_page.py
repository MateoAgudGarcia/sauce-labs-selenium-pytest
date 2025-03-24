from src.authorized_pages.checkout_complete_page import CheckoutComplete
from src.authorized_pages.authorized_page import AuthorizedPage
from src.summary_containers.cart_list import CartList
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import wait_for_element_to_be_visible


class OverviewPage(AuthorizedPage, CartList):
    def _checkout_summary_container(self) -> WebElement:
        return self.root_element.find_element(By.ID, "checkout_summary_container")

    def _subtotal_label(self) -> WebElement:
        return self._checkout_summary_container().find_element(
            By.CSS_SELECTOR, "div.summary_subtotal_label"
        )

    def _tax_label(self) -> WebElement:
        return self._checkout_summary_container().find_element(
            By.CSS_SELECTOR, "div.summary_tax_label"
        )

    def _total_label(self) -> WebElement:
        return self._checkout_summary_container().find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        )

    def _cart_footer(self) -> WebElement:
        return self._checkout_summary_container().find_element(
            By.CSS_SELECTOR, "div.cart_footer"
        )

    def _button_cancel(self) -> WebElement:
        return self._cart_footer().find_element(By.ID, "cancel")

    def _button_finish(self) -> WebElement:
        return self._cart_footer().find_element(By.ID, "finish")

    def verify_subtotal(self, subtotal: str) -> None:
        """
        Verify the subtotal of the order.

        Args:
            subtotal : str
                The expected subtotal value.
        """
        wait_for_element_to_be_visible(self.driver, self._subtotal_label())
        assert subtotal in self._subtotal_label().text

    def verify_tax(self, tax: str) -> None:
        """
        Verify the tax of the order.

        Args:
            tax : str
                The expected tax value.
        """
        wait_for_element_to_be_visible(self.driver, self._tax_label())
        assert tax in self._tax_label().text

    def verify_total(self, total: str) -> None:
        """
        Verify the total of the order.

        Args:
            total : str
                The expected total value.
        """
        wait_for_element_to_be_visible(self.driver, self._total_label())
        assert total in self._total_label().text

    def go_to_completed_order(self) -> CheckoutComplete:
        """
        Click on the Finish button to complete the order.

        Returns:
            CheckoutComplete: An instance of the CheckoutComplete class.
        """
        wait_for_element_to_be_visible(self.driver, self._button_finish())
        self._button_finish().click()
        return CheckoutComplete(self.driver)
