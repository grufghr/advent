Feature: AoC 2021 Day 09: Smoke Basin

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 15       |
      | tc02 | part01 | "input.txt"         | 518      |
      | tc03 | part02 | "input_example.txt" | 1134     |
      | tc04 | part02 | "input.txt"         | 949905   |
