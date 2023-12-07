Feature: AoC 2015 Day 12: JSAbacusFramework.io

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 33       |
      | tc02 | part01 | "input.txt"         | 111754   |
      | tc03 | part02 | "input_example.txt" | 16       |
      | tc04 | part02 | "input.txt"         | 65402    |
