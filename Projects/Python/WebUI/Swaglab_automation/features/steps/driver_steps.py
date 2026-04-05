from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.driver_factory import get_browser


@given("user opens the test website")
def step_open_site(context):
    context.driver = get_browser()
    context.driver.get("http://info.cern.ch")


@when("user collects all links")
def step_get_links(context):
    context.links = context.driver.find_elements(By.TAG_NAME, "a")


@then("links should be validated")
def step_validate_links(context):
    print("Total links:", len(context.links))

    assert len(context.links) > 2

    for link in context.links:
        href = link.get_attribute("href")
        if href:
            print(href)

    context.driver.quit()