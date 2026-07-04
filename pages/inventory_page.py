from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.cart_page import CartPage

class InventoryPage(BasePage):

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    BACKPACK_ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
   
    
    
    
    
    
    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_loaded(self):
        return self.wait_for_element(
            self.INVENTORY_CONTAINER
        ).is_displayed()

    def get_product_count(self):
        products = self.find_elements(self.PRODUCTS)
        return len(products)
    
    def add_to_cart(self):
        self.click(self.BACKPACK_ADD_TO_CART)

    def get_cart_badge_count(self):
        badge = self.wait_for_element(self.CART_BADGE)
        text = badge.text
        badge_count = int(text)
        return badge_count

    def click_cart(self):
        self.click(self.CART_ICON)
        return CartPage(self.driver)
    

    

        