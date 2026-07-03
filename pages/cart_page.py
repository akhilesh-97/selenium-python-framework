from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.CheckoutInfoPage import CheckoutInfoPage

class CartPage(BasePage):

    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    
    def is_item_present(self):
        item = self.wait_for_element(self.ITEM_NAME)
        item_text = item.text
        return item_text == "Sauce Labs Backpack"

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
        return CheckoutInfoPage(self.driver)





