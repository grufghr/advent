Feature: AoC 2023 Day 11: Cosmic Expansion

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected     |
      | tc01 | part01 | "input_example.txt" | 374          |
      | tc02 | part01 | "input.txt"         | 9522407      |
      | tc03 | part02 | "input_example.txt" | 82000210     |
      | tc04 | part02 | "input.txt"         | 544723432977 |
