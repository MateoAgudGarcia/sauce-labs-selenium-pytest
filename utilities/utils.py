from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_to_be_clickable(driver: WebDriver, element: WebElement, timeout=5) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(element)
    )
