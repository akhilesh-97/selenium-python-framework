from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")


    def __init__(self, driver):
        super().__init__(driver)

    
    def is_item_present(self):
        item = self.wait_for_element(self.ITEM_NAME)
        item_text = item.text
        return item_text == "Sauce Labs Backpack"

