@wip
Feature: Get back to homepage functionality
  Background:
    Given User launch laptop and notebooks page

  @positive
  Scenario: a user can get back to home page by clicking on logo icon
    Given User is on the Laptops and Notebooks page
    When user click on Logo
    Then The user is able to lend on Homepage of the website
