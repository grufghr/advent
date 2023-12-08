Feature: AoC 2021 Day 05: Hydrothermal Venture

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 5        |
      | tc02 | part01 | "input.txt"         | 6666     |
      | tc03 | part02 | "input_example.txt" | 12       |
      | tc04 | part02 | "input.txt"         | 19081    |
