Feature: AoC 2022 Day 06: Tuning Trouble

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 6        |
      | tc02 | part01 | "input.txt"         | 1531     |
      | tc03 | part02 | "input_example.txt" | 23       |
      | tc04 | part02 | "input.txt"         | 2518     |
