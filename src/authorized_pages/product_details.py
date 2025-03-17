from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.authorized_pages.shopping_cart_page import ShoppingCart
from src.authorized_pages.authorized_page import AuthorizedPage
from utilities.utils import (
    wait_for_element_to_be_clickable,
    wait_for_element_to_be_visible,
)


class ProductDetails(AuthorizedPage):
    def _inventory_item_container(self) -> WebElement:
        return self._contents_wrapper().find_element(
            By.CSS_SELECTOR, "div.inventory_item_container"
        )

    def _inventory_details_image_container(self) -> WebElement:
        return self._inventory_item_container().find_element(
            By.CSS_SELECTOR, "div.inventory_details_img_container"
        )

    def _inventory_details_image(self) -> WebElement:
        return self._inventory_details_image_container().find_element(
            By.CSS_SELECTOR, "img.inventory_details_img"
        )

    def _inventory_details_desc_container(self) -> WebElement:
        return self._inventory_item_container().find_element(
            By.CSS_SELECTOR, "div.inventory_details_desc_container"
        )

    def _inventory_details_name(self) -> WebElement:
        return self._inventory_details_desc_container().find_element(
            By.CSS_SELECTOR, "div.inventory_details_name"
        )

    def _inventory_details_description(self) -> WebElement:
        return self._inventory_details_desc_container().find_element(
            By.CSS_SELECTOR, "div.inventory_details_desc"
        )

    def _inventory_details_price(self) -> WebElement:
        return self._inventory_details_desc_container().find_element(
            By.CSS_SELECTOR, "div.inventory_details_price"
        )

    def _add_to_cart_button(self) -> WebElement:
        return self._inventory_details_desc_container().find_element(
            By.ID, "add-to-cart"
        )

    def _remove_from_cart_button(self) -> WebElement:
        return self._inventory_details_desc_container().find_element(By.ID, "remove")

    def verify_product_price(self, price: str):
        """
        Verify that the product price is equal to the given price
        """
        wait_for_element_to_be_visible(self.driver, self._inventory_item_container())
        wait_for_element_to_be_visible(self.driver, self._inventory_details_price())
        assert self._inventory_details_price().text == price

    def add_product_to_cart(self):
        """
        Add the product to the cart
        """
        wait_for_element_to_be_visible(self.driver, self._add_to_cart_button())
        self._add_to_cart_button().click()

    def remove_product_from_cart(self):
        """
        Remove the product from the cart
        """
        wait_for_element_to_be_visible(self.driver, self._remove_from_cart_button())
        self._remove_from_cart_button().click()

    def go_to_shopping_cart(self) -> ShoppingCart:
        """
        Go to the shopping cart page
        """
        wait_for_element_to_be_clickable(self.driver, self._shopping_cart_link())
        self._shopping_cart_link().click()
        return ShoppingCart(self.driver)
