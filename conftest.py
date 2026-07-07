import os
from datetime import datetime

import pytest

from utilities.driver_factory import DriverFactory
from utilities.logger import LogGenerator
from utilities.config import Config


@pytest.fixture
def driver(request):

    logger = LogGenerator.log()

    driver = DriverFactory.get_driver(
        Config.BROWSER
    )

    logger.info(f"Launching {Config.BROWSER.capitalize()} Browser")

    driver.get(
        Config.BASE_URL
    )

    logger.info(f"Navigated to  {Config.BASE_URL} ")

    #  Give the current test access to the driver
    request.node.driver = driver

    yield driver

    logger.info("Closing Browser")
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
        logger = LogGenerator.log()

        if driver is not None:
            try:    
                os.makedirs("screenshots", exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{item.name}_{timestamp}.png"
                filepath = os.path.join("screenshots", filename)

                driver.save_screenshot(filepath)

                
                logger.info(f"Screenshot saved: {filepath}")

            except Exception as e:
                logger.error(f"Screenshot capture failed: {e} ")
