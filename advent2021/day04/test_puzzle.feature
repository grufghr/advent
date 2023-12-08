Feature: AoC 2021 Day 04: Giant Squid

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 4512     |
      | tc02 | part01 | "input.txt"         | 64084    |
      | tc03 | part02 | "input_example.txt" | 1924     |
      | tc04 | part02 | "input.txt"         | 12833    |
