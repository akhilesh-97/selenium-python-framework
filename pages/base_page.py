
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utilities.config import Config

class BasePage:


    def __init__(self, driver):
        self.driver = driver
    
    def get_title(self):
        return self.driver.title
    
    def get_current_url(self):
        return self.driver.current_url
    
    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()
        

    def type(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)
    
    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, Config.TIMEOUT)
       
        return wait.until(
             EC.visibility_of_element_located(locator)
        )
    
    def find_elements(self, locator):

        return self.driver.find_elements(*locator)