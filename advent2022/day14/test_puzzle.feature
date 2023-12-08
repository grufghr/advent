Feature: AoC 2022 Day 14: Regolith Reservoir

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 24       |
      | tc02 | part01 | "input.txt"         | 913      |
      | tc03 | part02 | "input_example.txt" | 93       |
      | tc04 | part02 | "input.txt"         | 30762    |
