Feature: AoC 2022 Day 13: Distress Signal

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 13       |
      | tc02 | part01 | "input.txt"         | 5806     |
      | tc03 | part02 | "input_example.txt" | 140      |
      | tc04 | part02 | "input.txt"         | 23600    |
