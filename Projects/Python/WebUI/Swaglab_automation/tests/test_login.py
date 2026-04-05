# Test: Valid login

from utils.driver_factory import get_browser
from utils import config
from pages import login_page


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