@wip
Feature: Add to wishlist functionality

  @positive
  Scenario: a user can click on Add to wishlist button
    Given User is on the PC page
    When user click on Add to Wishlist button
    Then User is be able to see the item in the wish list
