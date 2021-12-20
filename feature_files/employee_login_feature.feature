Feature: The website should be able to login an employee

  Scenario: As an Employee I should be able to login
    Given The user is on the website home page
    When The user inputs credentials and clicks on the login button
    Then The user should be redirected to the employee page