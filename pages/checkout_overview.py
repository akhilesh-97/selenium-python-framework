from pages.base_page import BasePage
from pages.comlpete_order import CheckoutCompletePage
from selenium.webdriver.common.by import By

class CheckoutOverviewPage(BasePage):


    FINISH_BTN = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def click_finish(self):
        self.click(self.FINISH_BTN)
        return CheckoutCompletePage(self.driver)
    

    


