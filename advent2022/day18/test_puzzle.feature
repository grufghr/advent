Feature: AoC 2022 Day 18: Boiling Boulders

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
      | tc01 | part01 | "input_example.txt" | 64       |
      | tc02 | part01 | "input.txt"         | 3364     |
      | tc03 | part02 | "input_example.txt" | 58       |
      | tc04 | part02 | "input.txt"         | 2006     |
