# Driver test - extract links 

from selenium.webdriver.common.by import By
from utils.driver_factory import get_browser


def test_driver():

    # Launch browser
    driver = get_browser()

    # Open  site
    driver.get("http://info.cern.ch")

    # Get all links
    links = driver.find_elements(By.TAG_NAME, "a")

    print("Total links:", len(links))

    # Validation 
    assert len(links) > 2

    # Print links
    for link in links:
        href = link.get_attribute("href")
        if href:
            print(href)

    # Close browser
    driver.quit()