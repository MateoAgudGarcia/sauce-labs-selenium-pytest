import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@allure.parent_suite("Search - Homepage")
@allure.suite("Google Tests")
@allure.title("Google page should have 'Google' in the title")
def test_google_title(driver):
    with allure.step("Open Google page"):
        driver.get("https://www.google.com")

    with allure.step("Check the title"):
        assert 'Google' in driver.title

@allure.parent_suite("Search - Homepage")
@allure.suite("Google Tests")
@allure.title("Google page should have a search input element")
def test_google_search_input(driver):
    with allure.step("Open Google page"):
        driver.get("https://www.google.com")

    with allure.step("Find the search input element"):
        search_input = driver.find_element(By.NAME, "q")
        visibility = search_input.is_displayed()
        assert visibility is True
