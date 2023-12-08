Feature: AoC 2022 Day 12: Hill Climbing Algorithm

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
      | tc01 | part01 | "input_example.txt" | 31       |
      | tc02 | part01 | "input.txt"         | 456      |
      | tc03 | part02 | "input_example.txt" | 29       |
      | tc04 | part02 | "input.txt"         | 454      |
