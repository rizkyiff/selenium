import sys
import os

# Add the base directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_object.example_page import ExamplePage

@pytest.fixture
def driver():
    """Setup and teardown for the WebDriver."""
    # Initialize WebDriver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_click_element(driver):
    """Test case to click an element on the page."""
    # Initialize page object
    page = ExamplePage(driver)
    
    # Open the page
    page.open("https://www.example.com")  # Replace with the actual URL
    
    # Click the element
    page.click_element()
    
    # Optionally, add assertions here to verify the result of the click action
    assert driver.title == "Example Domains"  # Replace with the expected title or condition

if __name__ == "__main__":
    pytest.main()
