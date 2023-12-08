Feature: AoC 2015 Day 13: Knights of the Dinner Table

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 330      |
      | tc02 | part01 | "input.txt"         | 664      |
      | tc03 | part02 | "input_example.txt" | 286      |
      | tc04 | part02 | "input.txt"         | 640      |
