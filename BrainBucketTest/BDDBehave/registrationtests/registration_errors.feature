Feature: Error messages during registration process

  Scenario Outline: enter in "<field>" "<type>" value
    Given user on the registration page
    When user types "<value>" in "<field>"
    And user clicks Continue button
    Then error is shown under "<field>" field

  Examples:
    | field       | type  | value                             |
    | first_name  | short | None                                |
    | last_name   | short | None                                |
    | first_name  | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    | last_name   | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    | phonenumber | short | 12                                |
    | phonenumber | long  | 123456789123456789123456789123456 |
    | password    | short | Aa1                               |
    | password    | long  | 123456789123456789aAs             |