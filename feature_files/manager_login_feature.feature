Feature: The website should be able to login a manager

  Scenario: As an Manager I should be able to login
    Given The user is on the website home page
    When The user inputs credentials and clicks on the login button
    Then The user should be redirected to the manager page