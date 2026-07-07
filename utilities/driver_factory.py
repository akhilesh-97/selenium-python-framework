from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.config import Config


class DriverFactory:

    @staticmethod
    def get_driver(browser=None):

        browser = (browser or Config.BROWSER).lower()

        if browser == "chrome":

            options = ChromeOptions()

            # ----------------------------
            # Headless Mode
            # ----------------------------
            if Config.HEADLESS:
                options.add_argument("--headless=new")

            # ----------------------------
            # Browser Options
            # ----------------------------
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-save-password-bubble")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-infobars")

            # ----------------------------
            # Disable Password Manager
            # ----------------------------
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            }

            options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        elif browser == "firefox":

            options = FirefoxOptions()

            if Config.HEADLESS:
                options.add_argument("-headless")

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

            driver.maximize_window()

        elif browser == "edge":

            options = EdgeOptions()

            if Config.HEADLESS:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return driver