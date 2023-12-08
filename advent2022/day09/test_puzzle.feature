Feature: AoC 2022 Day 09: Rope Bridge

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 88       |
      | tc02 | part01 | "input.txt"         | 6175     |
      | tc03 | part02 | "input_example.txt" | 36       |
      | tc04 | part02 | "input.txt"         | 2578     |
