Feature: Privacy Policy Checkbox functionality
  Background:
    Given User launch register page

  Scenario: a user can login using correct email and password
    Given User is entered all cridentials in the fields to create an account
    When user click onm the Agree on Privacy Policy checkbox
    Then The user is able to check Privacy policy checkbox
