from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.authorized_pages.authorized_page import AuthorizedPage
from utilities.utils import wait_for_element_to_be_visible


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

    def verify_product_price(self, price: str):
        wait_for_element_to_be_visible(self.driver, self._inventory_item_container())
        wait_for_element_to_be_visible(self.driver, self._inventory_details_price())
        assert self._inventory_details_price().text == price
