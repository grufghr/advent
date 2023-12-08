Feature: AoC 2016 Day 05: How About a Nice Game of Chess?

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
      | tc01 | part01 | "input_example.txt" | 18f47a30 |
      | tc02 | part01 | "input.txt"         | f97c354d |
      | tc03 | part02 | "input_example.txt" | 05ace8e3 |
      | tc04 | part02 | "input.txt"         | 863dde27 |
