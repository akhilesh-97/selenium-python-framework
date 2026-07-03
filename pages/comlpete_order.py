from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    HOME_BTN = (By.ID, "back-to-products")


    def __init__(self, driver):
        super().__init__(driver)

    def is_order_completed(self):
        header = self.wait_for_element(self.COMPLETE_HEADER)
        return header.text == "Thank you for your order!"
    
    def click_back_home(self):
        from pages.inventory_page import InventoryPage

        self.click(self.HOME_BTN)
        return InventoryPage(self.driver)
    

        
    

