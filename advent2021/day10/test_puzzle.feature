Feature: AoC 2021 Day 10: Syntax Scoring

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected   |
      | tc01 | part01 | "input_example.txt" | 26397      |
      | tc02 | part01 | "input.txt"         | 339477     |
      | tc03 | part02 | "input_example.txt" | 288957     |
      | tc04 | part02 | "input.txt"         | 3049320156 |
