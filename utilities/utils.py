from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_to_be_clickable(
    driver: WebDriver, element: WebElement, timeout=5
) -> WebElement:
    """
    Wait for an element to be clickable
    """
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(element))


def wait_for_element_to_be_visible(
    driver: WebDriver, element: WebElement, timeout=5
) -> WebElement:
    """
    Wait for an element to be visible
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of(element))
