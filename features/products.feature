Feature: Product management
  Scenario: List all products
    When I visit the "Home Page"
    Then I should see "Products"

  Scenario: Create a product
    When I set the "Name" to "Phone"
    And I press the "Create" button
    Then I should see "Phone"

  Scenario: Update a product
    Given the following products
      | name  | category     | available | price |
      | Phone | Electronics  | True      | 499.99 |
    When I change the "Name" to "Smartphone"
    Then I should see "Smartphone"

  Scenario: Delete a product
    When I press the "Delete" button
    Then I should not see "Phone"