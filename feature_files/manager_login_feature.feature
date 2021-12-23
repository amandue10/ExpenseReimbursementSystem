Feature: The website should be able to login a Manager

  Scenario: As an Manager I should be able to login
    Given Manager is on the login page
    When Manager inputs 1 into Manager Id field
    When Manager inputs Amanda into first name field
    When Manager inputs Jones into last name field
    When Manager inputs password into password field
    When Manager clicks submit button
    Then Manager should be redirected to the webpage with the title Manager Request Page

    Scenario: As a Manager I should be able to approve, deny and leave a comment on reimbursement requests
      Given The manager is on the manager home page
      When manager inputs 6 into reimbursement Id field
      When manager inputs 3 into logged in employee Id field
      When manager inputs 1 into manager id field
      When manager inputs 200 into amount requested field
      When manager inputs employee comment into comment field
      When manager inputs manager comment into comment field
      When manager chooses approved status from drop down box
      When manager inputs 12/18/2021 into request date field
      When manager clicks submit button to create a request
    Then the manager should have updated the reimbursement request


    Scenario: As an Manager I should be able to logout
    Given The logged in manager is on the Manager page
    When The manager clicks on the logout button
    Then The manager should be redirected to the home page