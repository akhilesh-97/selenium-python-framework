import pytest
from utilities.config_reader import get_base_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import LogGenerator
import os 
from datetime import datetime



@pytest.fixture
def driver(request):

    logger = LogGenerator.log()

    logger.info("Launching Chrome Browser")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()
    driver.get(get_base_url())

    logger.info("Navigated to Swag Labs")

    #  Give the current test access to the driver
    request.node.driver = driver

    yield driver

    driver.quit()


# ------------------------------------
# HOOK Function
# ------------------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Attach the report to the item
    setattr(item, "rep_" + report.when, report)

    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join("screenshots", filename)

            driver.save_screenshot(filepath)

            print(f"Screenshot saved: {filepath}")