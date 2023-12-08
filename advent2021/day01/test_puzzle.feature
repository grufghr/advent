Feature: AoC 2021 Day 01: Sonar Sweep
  
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 7        |
      | tc02 | part01 | "input.txt"         | 1139     |
      | tc03 | part02 | "input_example.txt" | 5        |
      | tc04 | part02 | "input.txt"         | 1103     |
