Feature: AoC 2015 Day 11: Corporate Policy

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 4 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | abcdffaa |
      | tc02 | part01 | "input.txt"         | cqjxxyzz |

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input <input>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 4 secs
    Examples:
      | name | part   | input      | expected |
      | tc03 | part02 | "cqjxjnds" | cqjxxyzz |
      | tc03 | part02 | "cqjxxyzz" | cqkaabcc |
