import allure
from selenium.webdriver.common.by import By

@allure.parent_suite("Search - Homepage")
@allure.suite("Google Tests")
@allure.title("Google page should have 'Google' in the title")
def test_google_title(driver):
    with allure.step("Open Google page"):
        driver.get("https://www.google.com")

    with allure.step("Check the title"):
        assert 'Google' == driver.title

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
