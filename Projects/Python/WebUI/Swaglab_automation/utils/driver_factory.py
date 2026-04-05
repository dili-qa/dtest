from selenium import webdriver

def get_browser():

    # Create browser options
    browser_options = webdriver.EdgeOptions()

    # Start maximized
    browser_options.add_argument("--start-maximized")

    # Launch browser
    browser = webdriver.Edge(options=browser_options)

    return browser