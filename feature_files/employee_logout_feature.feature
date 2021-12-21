Feature: The website should be able to logout an employee

  Scenario: As an Employee I should be able to logout
    Given The Employee is on the employee page
    When The Employee clicks on the logout button
    Then The Employee should be redirected to the home page