Feature: AoC 2015 Day 02: I Was Told There Would Be No Math

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 101      |
      | tc02 | part01 | "input.txt"         | 1586300  |
      | tc03 | part02 | "input_example.txt" | 48       |
      | tc04 | part02 | "input.txt"         | 3737498  |
