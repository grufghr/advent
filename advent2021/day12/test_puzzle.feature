Feature: AoC 2021 Day 12: Passage Pathing

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 15 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 10       |
      | tc02 | part01 | "input.txt"         | 5212     |
      | tc03 | part02 | "input_example.txt" | 36       |
      | tc04 | part02 | "input.txt"         | 134862   |
