from src.authorized_pages.authorized_page import AuthorizedPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import wait_for_element_to_be_clickable


class CheckoutComplete(AuthorizedPage):
    def _checkout_complete_container(self) -> WebElement:
        return self.root_element.find_element(By.ID, "checkout_complete_container")

    def _complete_header(self) -> WebElement:
        return self._checkout_complete_container().find_element(
            By.CSS_SELECTOR, "h2.complete-header"
        )

    def _complete_text(self) -> WebElement:
        return self._checkout_complete_container().find_element(
            By.CSS_SELECTOR, "div.complete-text"
        )

    def _back_to_products(self) -> WebElement:
        return self._checkout_complete_container().find_element(
            By.ID, "back-to-products"
        )

    def verify_checkout_is_completed(self):
        """
        Verify that the checkout is completed
        """
        assert self._complete_header().text == "Thank you for your order!"
        assert (
            self._complete_text().text
            == "Your order has been dispatched, and will arrive"
            + " just as fast as the pony can get there!"
        )

    def go_back_to_products(self):
        """
        Click on Back to Products button
        """
        wait_for_element_to_be_clickable(self.driver, self._back_to_products())
        self._back_to_products().click()
