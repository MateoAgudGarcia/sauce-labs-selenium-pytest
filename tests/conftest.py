import platform
import os
import base64
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import selenium
import sys


@pytest.fixture(autouse=True)
def driver():
    os.makedirs("allure-results", exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    chrome_version = driver.capabilities["browserVersion"]

    os_info = platform.system() + " " + platform.release()
    python_version = sys.version.split(" ")[0]
    selenium_version = selenium.__version__

    with open("allure-results/environment.properties", "w") as f:
        f.write(f"Python.Version={python_version}\n")
        f.write(f"Selenium.Version={selenium_version}\n")
        f.write("Browser=Chrome\n")
        f.write(f"Browser.Version={chrome_version}\n")
        f.write(f"Platform={os_info}\n")

    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot = driver.get_screenshot_as_base64()
            allure.attach(
                base64.b64decode(screenshot),
                name="Screenshot on failure",
                attachment_type=AttachmentType.PNG,
            )
