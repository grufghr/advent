Feature: AoC 2016 Day 03: Squares With Three Sides

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 4        |
      | tc02 | part01 | "input.txt"         | 869      |
      | tc03 | part02 | "input_example.txt" | 7        |
      | tc04 | part02 | "input.txt"         | 1544     |
