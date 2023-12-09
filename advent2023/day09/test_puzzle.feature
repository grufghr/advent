Feature: AoC 2023 Day 09: Mirage Maintenance

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected   |
      | tc01 | part01 | "input_example.txt" | 114        |
      | tc02 | part01 | "input.txt"         | 1743490457 |
      | tc03 | part02 | "input_example.txt" | 2          |
      | tc04 | part02 | "input.txt"         | 1053       |
