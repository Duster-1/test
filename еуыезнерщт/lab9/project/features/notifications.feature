Feature: User Notifications

  Scenario: Viewing user notifications
    Given the user is logged in
    When the user navigates to the notifications page
    Then the user sees notifications
