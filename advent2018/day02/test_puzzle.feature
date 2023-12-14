Feature: AoC 2018 Day 02: Inventory Management System

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename               | expected                  |
      | tc01 | part01 | "input_example_01.txt" | 12                        |
      | tc02 | part01 | "input.txt"            | 7163                      |
      | tc03 | part02 | "input_example_02.txt" | fgij                      |
      | tc04 | part02 | "input.txt"            | ighfbyijnoumxjlxevacpwqtr |

