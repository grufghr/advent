Feature: AoC 2021 Day 11: Dumbo Octopus

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 1656     |
      | tc02 | part01 | "input.txt"         | 1637     |
      | tc03 | part02 | "input_example.txt" | 195      |
      | tc04 | part02 | "input.txt"         | 242      |
