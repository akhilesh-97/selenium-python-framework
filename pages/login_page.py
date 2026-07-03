from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from utilities.logger import LogGenerator

class LoginPage(BasePage):
    
    logger = LogGenerator.log()

   
    def __init__(self, driver):
        super().__init__(driver)


    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):

        self.logger.info("Logging in with valid credentials")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

        self.logger.info("login successful")

        return InventoryPage(self.driver)
    
   