Feature: AoC 2018 Day 01: Chronal Calibration

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 0        |
      | tc02 | part01 | "input.txt"         | 599      |
      | tc03 | part02 | "input_example.txt" | 6        |
      | tc04 | part02 | "input.txt"         | 81204    |
