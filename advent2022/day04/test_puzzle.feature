Feature: AoC 2022 Day 04: Camp Cleanup

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 2        |
      | tc02 | part01 | "input.txt"         | 413      |
      | tc03 | part02 | "input_example.txt" | 4        |
      | tc04 | part02 | "input.txt"         | 806      |
