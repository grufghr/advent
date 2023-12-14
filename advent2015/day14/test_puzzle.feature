Feature: AoC 2015 Day 14: Reindeer Olympics

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 7 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 1120     |
      | tc02 | part01 | "input.txt"         | 2696     |
      | tc03 | part02 | "input_example.txt" | 689      |
      | tc04 | part02 | "input.txt"         | 1084     |
