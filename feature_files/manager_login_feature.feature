Feature: The website should be able to login a Manager

  Scenario: As an Manager I should be able to login
    Given Manager is on the login page
    When Manager inputs <manager id> into Manager Id field
    When Manager inputs <first name> into first name field
    When Manager inputs <last name> into last name field
    When Manager inputs <password> into password field
    When Manager clicks submit button
    Then Manager should be redirected to the webpage with the title Manager page