from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExamplePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url):
        """Open the given URL."""
        self.driver.get(url)
    
    def get_element(self):
        """Wait for the element to be clickable and return it."""
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/p[2]/a"))
        )
    
    def click_element(self):
        """Click the element."""
        element = self.get_element()
        element.click()
