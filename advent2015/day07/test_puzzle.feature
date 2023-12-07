Feature: AoC 2015 Day 07: Some Assembly Required

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 65079    |
      | tc02 | part01 | "input.txt"         | 16076    |
      | tc03 | part02 | "input_example.txt" | 65079    |
      | tc04 | part02 | "input.txt"         | 2797     |
