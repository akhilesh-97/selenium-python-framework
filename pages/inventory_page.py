from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_loaded(self):
        return self.wait_for_element(
            self.INVENTORY_CONTAINER
        ).is_displayed()

    def get_product_count(self):
        products = self.find_elements(self.PRODUCTS)
        return len(products)