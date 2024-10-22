Feature: AoC 2020 Day 03: Toboggan Trajectory

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected   |
      | tc01 | part01 | "input_example.txt" | 7          |
      | tc02 | part01 | "input.txt"         | 228        |
      | tc03 | part02 | "input_example.txt" | 336        |
      | tc04 | part02 | "input.txt"         | 6818112000 |
