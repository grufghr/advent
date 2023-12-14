Feature: AoC 2017 Day 03: Spiral Memory

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 31       |
      | tc02 | part01 | "input.txt"         | 371      |
      | tc03 | part02 | "input_example.txt" | 1968     |
      | tc04 | part02 | "input.txt"         | 369601   |
