Feature: AoC 2023 Day 15: Lens Library

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 10 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 1320     |
      | tc02 | part01 | "input.txt"         | 516657   |
      | tc03 | part02 | "input_example.txt" | 145      |
      | tc04 | part02 | "input.txt"         | 210906   |
