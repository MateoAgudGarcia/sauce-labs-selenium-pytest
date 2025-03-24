from src.authorized_pages.checkout_page import CheckoutPage
from src.authorized_pages.authorized_page import AuthorizedPage
from src.summary_containers.cart_list import CartList
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import wait_for_element_to_be_clickable


class ShoppingCart(AuthorizedPage, CartList):
    def _cart_contents_container(self) -> WebElement:
        return self.root_element.find_element(By.ID, "cart_contents_container")

    def _cart_list(self) -> WebElement:
        return self._cart_contents_container().find_element(
            By.CSS_SELECTOR, "div.cart_list"
        )

    def _remove_product_by_index(self, index: int = 0) -> WebElement:
        return self._item_price_bar_by_index(index).find_element(
            By.CSS_SELECTOR, "button.cart_button[id^='remove']"
        )

    def _cart_footer(self) -> WebElement:
        return self._cart_contents_container().find_element(
            By.CSS_SELECTOR, "div.cart_footer"
        )

    def _button_continue_shopping(self) -> WebElement:
        return self._cart_footer().find_element(By.ID, "continue-shopping")

    def _button_checkout(self) -> WebElement:
        return self._cart_footer().find_element(By.ID, "checkout")

    def remove_product_by_index(self, index: int = 0) -> None:
        """
        Remove a product from the cart by its index.

        Args:
            index : int
                The index of the product to remove from the cart.
        """
        wait_for_element_to_be_clickable(self.driver, self._remove_product_by_index(index))
        self._remove_product_by_index(index).click()

    def go_to_checkout(self) -> CheckoutPage:
        """
        Click on the Checkout button to proceed to the checkout page.

        Returns:
            CheckoutPage: An instance of the CheckoutPage class.
        """
        wait_for_element_to_be_clickable(self.driver, self._button_checkout())
        self._button_checkout().click()
        return CheckoutPage(self.driver)
