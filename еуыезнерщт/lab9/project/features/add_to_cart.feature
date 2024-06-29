Feature: Add product to cart

  Scenario: Adding a product to the cart
    Given the user is on the home page
    When the user searches for "Ноутбук"
    And the user adds the first product to the cart
    Then the product "Ноутбук" is in the cart
