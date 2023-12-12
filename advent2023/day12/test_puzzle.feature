Feature: AoC 2023 Day 12: Hot Springs

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 3 secs
    Examples:
      | name | part   | filename            | expected       |
      | tc01 | part01 | "input_example.txt" | 21             |
      | tc02 | part01 | "input.txt"         | 7025           |
      | tc03 | part02 | "input_example.txt" | 525152         |
      | tc04 | part02 | "input.txt"         | 11461095383315 |
