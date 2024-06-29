Feature: User Registration

  Scenario: Successful user registration
    Given the user is on the registration page
    When the user registers with email "test@example.com" and password "Password123"
    Then the user sees a registration success message
