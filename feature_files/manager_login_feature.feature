Feature: The website should be able to login a Manager

  Scenario: As an Manager I should be able to login
    Given Manager is on the login page
    When Manager inputs <1> into Manager Id field
    When Manager inputs <Henry> into first name field
    When Manager inputs <Cantu> into last name field
    When Manager inputs <password> into password field
    When Manager clicks submit button
    Then Manager should be redirected to the webpage with the title Manager home page