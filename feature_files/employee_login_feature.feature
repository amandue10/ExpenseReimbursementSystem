Feature: The website should be able to login an employee

  Scenario: As an Employee I should be able to login
    Given Employee is on the login page
    When Employee inputs 1 into employee Id field
    When Employee inputs Henry into first name field
    When Employee inputs Cantu into last name field
    When Employee inputs password into password field
    When Employee clicks submit button
    Then Employee should be redirected to the webpage with the title employee page