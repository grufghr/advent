Feature: AoC 2023 Day 05: If You Give A Seed A Fertilizer

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected  |
      | tc01 | part01 | "input_example.txt" | 35        |
      | tc02 | part01 | "input.txt"         | 227653707 |
      | tc03 | part02 | "input_example.txt" | 46        |
      | tc04 | part02 | "input.txt"         | 78775051  |
