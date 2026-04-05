Feature: Login functionality

  Scenario: Valid user login
    Given user is on login page
    When user logs in with valid credentials
    Then user should be logged in successfully

  Scenario: Invalid user login
    Given user is on login page
    When user logs in with invalid credentials
    Then user should see login error message
