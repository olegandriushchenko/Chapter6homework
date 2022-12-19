Feature: Products
  Scenario: A user can add product to the wishlist
    Given user on the homepage
    When user click on Add to Wishlist button on the product
    Then user will be able to see the this product in the wishlist
    