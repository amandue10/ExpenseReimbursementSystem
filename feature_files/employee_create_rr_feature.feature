Feature: The website should be able to create a reimbursement request

  Scenario: As an Employee I should be able to create a reimbursement request
    Given The user is on the employee page
    When the user inputs <value> into the input boxes
    When the user clicks the create button
    Then the user should have created a new reimbursement request