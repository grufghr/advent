Feature: AoC 2015 Day 08: Matchsticks

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 12       |
      | tc02 | part01 | "input.txt"         | 1371     |
      | tc03 | part02 | "input_example.txt" | 19       |
      | tc04 | part02 | "input.txt"         | 2117     |
