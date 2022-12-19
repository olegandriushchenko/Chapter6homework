Feature: Add to cart feature
  Background:
    Given User launch Desktops, PC page

  Scenario: a user can add to cart product
    Given User is on the PC page
    When user click on the Add to Cart button
    And User clicks on the Shopping cart button
    Then User should be able to see saved items in the Shopping Cart

