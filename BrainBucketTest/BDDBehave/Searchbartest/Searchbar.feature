@wip
Feature: Searchbar functionality

  @positive
  Scenario: a user can click, type in and search product on the website through searchbar
    Given User is click on the searchbar
    When user enters product that he want to find
    Then The user should see the list with products that he wanted to find
