from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.authorized_pages.product_details import ProductDetails
from src.authorized_pages.authorized_page import AuthorizedPage
from utilities.utils import wait_for_element_to_be_clickable


class InventoryPage(AuthorizedPage):

    def _product_select_container(self) -> WebElement:
        return self.root_element.find_element(By.CSS_SELECTOR, "span.select_container")

    def _active_option(self) -> WebElement:
        return self._product_select_container().find_element(
            By.CSS_SELECTOR, "span.active_option"
        )

    def _product_sort_container(self) -> WebElement:
        return self._product_select_container().find_element(
            By.CSS_SELECTOR, "select.product_sort_container"
        )

    def _inventory_container(self) -> WebElement:
        return self._contents_wrapper().find_element(By.ID, "inventory_container")

    def _inventory_list(self) -> WebElement:
        return self._inventory_container().find_element(
            By.CSS_SELECTOR, "div.inventory_list"
        )

    def _list_of_products(self) -> List[WebElement]:
        return self._inventory_list().find_elements(
            By.CSS_SELECTOR, "div.inventory_item"
        )

    def _product_title_link_by_index(self, index: int) -> WebElement:
        return self._list_of_products()[index].find_element(
            By.CSS_SELECTOR, "a[id$='title_link']"
        )

    def select_product_sort(self, value: str):
        """
        Select the product sort option
        """
        select_product_sort = Select(self._product_sort_container())
        select_product_sort.select_by_visible_text(value)
        assert self._active_option().text == value

    def open_product_details(self, product_index: int) -> ProductDetails:
        """
        Open the product details page
        """
        product = self._product_title_link_by_index(product_index)
        wait_for_element_to_be_clickable(self.driver, product)
        product.click()
        return ProductDetails(self.driver)
