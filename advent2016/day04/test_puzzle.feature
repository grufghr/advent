Feature: AoC 2016 Day 04: Security Through Obscurity

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 2181     |
      | tc02 | part01 | "input.txt"         | 245102   |
      | tc03 | part02 | "input_example.txt" | 324      |
      | tc04 | part02 | "input.txt"         | 324      |
