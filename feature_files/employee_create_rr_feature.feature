#Feature: The website should be able to create a reimbursement request
#
#  Scenario: As an Employee I should be able to create a reimbursement request
#    Given The Employee is on the employee page
#    When Employee inputs 1 into reimbursement Id field
#    When Employee inputs 1 into employee Id field
#    When Employee inputs 1 into manager id field
#    When Employee inputs 200 into amount requested field
#    When Employee inputs comment into comment field
#    When Employee inputs 12/18/2021 into request date field
#    When Employee clicks submit button
#    Then the Employee should have created a new reimbursement request