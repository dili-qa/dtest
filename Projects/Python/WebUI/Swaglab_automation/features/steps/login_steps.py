from behave import given, when, then
from utils.driver_factory import get_browser
from utils import config
from pages import login_page


@given("user is on login page")
def step_open_login(context):
    context.driver = get_browser()
    context.driver.get(config.BASE_URL)


@when("user logs in with valid credentials")
def step_valid_login(context):
    login_page.login(
        context.driver,
        config.USERNAME,
        config.PASSWORD
    )


@when("user logs in with invalid credentials")
def step_invalid_login(context):
    login_page.login(
        context.driver,
        "wrong_user",
        "wrong_password"
    )


@then("user should be logged in successfully")
def step_verify_success(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()


@then("user should see login error message")
def step_verify_error(context):
    error = context.driver.find_element(
        "css selector",
        "h3[data-test='error']"
    ).text

    print("Error message:", error)

    assert "do not match" in error
    context.driver.quit()