Feature: AoC 2023 Day 13: Point of Incidence

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 405      |
      | tc02 | part01 | "input.txt"         | 35691    |
      | tc03 | part02 | "input_example.txt" | 400      |
      | tc04 | part02 | "input.txt"         | 39037    |
