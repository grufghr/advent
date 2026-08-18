Feature: AoC 2023 Day 03: Gear Ratios

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected  |
      | tc01 | part01 | "input_example.txt" | 4361      |
      | tc02 | part01 | "input.txt"         | 520019    |
      | tc03 | part02 | "input_example.txt" | 467835    |
      | tc04 | part02 | "input.txt"         | 75519888  |
