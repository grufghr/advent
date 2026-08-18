Feature: AoC 2023 Day 01: Trebuchet?!

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename               | expected |
      | tc01 | part01 | "input_example_01.txt" | 142      |
      | tc02 | part01 | "input.txt"            | 54239    |
      | tc03 | part02 | "input_example_02.txt" | 281      |
      | tc04 | part02 | "input.txt"            | 55343    |
