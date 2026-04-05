# Login page actions 

from selenium.webdriver.common.by import By


def enter_username(driver, username):
    driver.find_element(By.ID, "user-name").send_keys(username)


def enter_password(driver, password):
    driver.find_element(By.ID, "password").send_keys(password)


def click_login(driver):
    driver.find_element(By.ID, "login-button").click()


def login(driver, username, password):
    enter_username(driver, username)
    enter_password(driver, password)
    click_login(driver)