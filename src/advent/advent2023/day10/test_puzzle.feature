Feature: AoC 2023 Day 10: Pipe Maze

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 4        |
      | tc02 | part01 | "input.txt"         | 6640     |
      | tc03 | part02 | "input_example.txt" | 1        |
      | tc04 | part02 | "input.txt"         | 411      |
