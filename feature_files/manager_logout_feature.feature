Feature: The website should be able to logout an Manager

  Scenario: As an Manager I should be able to logout
    Given The user is on the Manager page
    When The user clicks on the logout button
    Then The user should be redirected to the home page