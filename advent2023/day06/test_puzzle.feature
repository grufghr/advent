Feature: AoC 2023 Day 06: Wait For It

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 288      |
      | tc02 | part01 | "input.txt"         | 625968   |
      | tc03 | part02 | "input_example.txt" | 71503    |
      | tc04 | part02 | "input.txt"         | 43663323 |
