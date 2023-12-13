Feature: AoC 2017 Day 06: Memory Reallocation

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
      | tc02 | part01 | "input.txt"         | 12841    |
      | tc03 | part02 | "input_example.txt" | 4        |
      | tc04 | part02 | "input.txt"         | 8038     |
