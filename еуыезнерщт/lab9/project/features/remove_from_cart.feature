Feature: Remove product from cart

  Scenario: Removing a product from the cart
    Given the user is on the home page
    And the user has added a product to the cart
    When the user removes the product from the cart
    Then the cart is empty
