Feature: AoC 2015 Day 15: Science for Hungry People

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 62842880 |
      | tc02 | part01 | "input.txt"         | 21367368 |
      | tc03 | part02 | "input_example.txt" | 57600000 |
      | tc04 | part02 | "input.txt"         | 1766400  |
