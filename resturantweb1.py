from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

def scrape_with_selenium(url):
    driver.get(url)
    time.sleep(3)  # Allow time for the page to load fully

    restaurants = []
    try:
        # Adjusted selectors

            name = driver.find_element(By.CLASS_NAME, 'y-css-12x5mn4').text  # Confirm class name
            reviews = [rev.text for rev3 in driver.find_elements(By.CLASS_NAME, 'y-css-be55va')]

            restaurants.append({
                'name': name,
                'reviews': reviews
            })
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    return restaurants

# Usage
data = scrape_with_selenium("https://www.yelp.com")
print(data)
