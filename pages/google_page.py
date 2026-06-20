from pages.google_page import GooglePage


def test_google(driver):

    google = GooglePage(driver)

    google.open()

    assert "Google" in driver.title