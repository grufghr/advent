Feature: AoC 2017 Day 02: Corruption Checksum

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 18       |
      | tc02 | part01 | "input.txt"         | 58975    |
      | tc03 | part02 | "input_example.txt" | 9        |
      | tc04 | part02 | "input.txt"         | 308      |
