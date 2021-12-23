Feature: The website should be able to login an employee

  Scenario: As an Employee I should be able to login
    Given Employee is on the login page
    When Employee inputs 1 into employee Id field
    When Employee inputs Henry into first name field
    When Employee inputs Cantu into last name field
    When Employee inputs password into password field
    When Employee clicks submit button
    Then Employee should be redirected to the webpage with the title employee page

    Scenario: As an Employee I should be able to create a reimbursement request
    Given The logged in Employee is on the employee page
    When Employee inputs 1 into reimbursement Id field
    When Employee inputs 1 into logged in employee Id field
    When Employee inputs 1 into manager id field
    When Employee inputs 200 into amount requested field
    When Employee inputs comment into comment field
    When Employee inputs 12/18/2021 into request date field
    When Employee clicks submit button to create a request
    Then the Employee should have created a new reimbursement request

    Scenario: As an Employee I should be able review my reimbursement requests
    Given The employee is on the employee home page waiting to view all requests
    Then The employee should be able to view the reimbursement requests

    Scenario: As an Employee I should be able to logout
    Given The logged in Employee is on the employee page waiting to logout
    When The Employee clicks on the logout button
    Then The Employee should be redirected to the home page