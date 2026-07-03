from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.checkout_overview import CheckoutOverviewPage

class CheckoutInfoPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)


    def click_continue(self):
        self.click(self.CONTINUE_BTN)
        return CheckoutOverviewPage(self.driver)
    
    

    

     


