Feature: Driver basic validation

  Scenario: Extract all links from a page
    Given user opens the test website
    When user collects all links
    Then links should be validated