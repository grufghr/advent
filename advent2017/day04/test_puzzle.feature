Feature: AoC 2017 Day 04: High-Entropy Passphrases

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 1        |
      | tc02 | part01 | "input.txt"         | 325      |
      | tc03 | part02 | "input_example.txt" | 0        |
      | tc04 | part02 | "input.txt"         | 119      |
