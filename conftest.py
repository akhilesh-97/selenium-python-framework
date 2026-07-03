import pytest
from utilities.config_reader import get_base_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import LogGenerator


@pytest.fixture
def driver():

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

    yield driver

    driver.quit()