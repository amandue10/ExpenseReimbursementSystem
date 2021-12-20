Feature: The website should be able to logout an employee

  Scenario: As an Employee I should be able to logout
    Given The user is on the employee page
    When The user clicks on the logout button
    Then The user should be redirected to the home page