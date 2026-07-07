import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_URL = os.getenv(
        "BASE_URL",
        "https://www.saucedemo.com"
    )

    BROWSER = os.getenv(
        "BROWSER",
        "chrome"
    ).lower()

    TIMEOUT = int(
        os.getenv("TIMEOUT", 10)
    )

    HEADLESS = os.getenv(
        "HEADLESS",
        "False"
    ).lower() == "true"