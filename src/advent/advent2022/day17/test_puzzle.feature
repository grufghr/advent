Feature: AoC 2022 Day 17: Pyroclastic Flow

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected      |
      | tc01 | part01 | "input_example.txt" | 3068          |
      | tc02 | part01 | "input.txt"         | 3124          |
      | tc03 | part02 | "input_example.txt" | 1514285714288 |
      | tc04 | part02 | "input.txt"         | 1561176470569 |
