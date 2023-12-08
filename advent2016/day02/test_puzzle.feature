Feature: AoC 2016 Day 02: Bathroom Security

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 1985     |
      | tc02 | part01 | "input.txt"         | 12578    |
      | tc03 | part02 | "input_example.txt" | 5DB3     |
      | tc04 | part02 | "input.txt"         | 516DD    |