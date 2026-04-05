# Tests

from utils.driver_factory import get_browser
from utils import config
from pages import login_page

#valid login

def test_valid_login():

    # Launch browser
    driver = get_browser()

    # Open application
    driver.get(config.BASE_URL)

    # Perform login
    login_page.login(driver, config.USERNAME, config.PASSWORD)

    # Validation 
    assert "inventory" in driver.current_url

    # Close browser
    driver.quit()

#invalid login

def test_invalid_login():

    # Launch browser
    driver = get_browser()

    # Open application
    driver.get(config.BASE_URL)

    # Perform login with WRONG credentials
    login_page.login(driver, "wrong_user", "wrong_password")

    # Get error message
    error = driver.find_element("css selector", "h3[data-test='error']").text

    print("Error message:", error)

    # Validation
    assert "do not match" in error

    # Close browser
    driver.quit()