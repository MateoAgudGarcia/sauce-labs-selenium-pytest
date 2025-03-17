from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from utilities.utils import wait_for_element_to_be_visible


class CartList:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.root_element = self.driver.find_element(By.CSS_SELECTOR, "div.cart_list")

    def _cart_items(self) -> List[WebElement]:
        return self.root_element.find_elements(By.CSS_SELECTOR, "div.cart_item")

    def _item_quantity_by_index(self, index: int = 0) -> WebElement:
        return self._cart_items()[index].find_element(
            By.CSS_SELECTOR, "div.cart_quantity"
        )

    def _item_label_by_index(self, index: int = 0) -> WebElement:
        return self._cart_items()[index].find_element(
            By.CSS_SELECTOR, "div.cart_item_label"
        )

    def _item_title_link_by_index(self, index: int = 0) -> WebElement:
        return self._item_label_by_index(index).find_element(
            By.CSS_SELECTOR, "a[id$='title_link']"
        )

    def _item_description_by_index(self, index: int = 0) -> WebElement:
        return self._item_label_by_index(index).find_element(
            By.CSS_SELECTOR, "div.inventory_item_desc"
        )

    def _item_price_bar_by_index(self, index: int = 0) -> WebElement:
        return self._cart_items()[index].find_element(
            By.CSS_SELECTOR, "div.item_pricebar"
        )

    def _item_price_by_index(self, index: int = 0) -> WebElement:
        return self._item_price_bar_by_index(index).find_element(
            By.CSS_SELECTOR, "div.inventory_item_price"
        )

    def verify_price_by_product_index(self, index: int, price: str):
        """
        Verify price by product index - Position
        """
        wait_for_element_to_be_visible(
            self.driver, self._item_price_bar_by_index(index)
        )
        wait_for_element_to_be_visible(self.driver, self._item_price_by_index(index))
        assert self._item_price_by_index(index).text == price

    def verify_quantity_by_product_index(self, index: int, quantity: int):
        """
        Verify quantity by product index - Position
        """
        wait_for_element_to_be_visible(self.driver, self._cart_items()[index])
        wait_for_element_to_be_visible(self.driver, self._item_quantity_by_index(index))
        assert self._item_quantity_by_index(index).text == f"{quantity}"
