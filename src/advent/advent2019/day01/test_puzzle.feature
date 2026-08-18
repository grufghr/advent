Feature: AoC 2019 Day 01: The Tyranny of the Rocket Equation

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 34241    |
      | tc02 | part01 | "input.txt"         | 3448043  |
      | tc03 | part02 | "input_example.txt" | 51316    |
      | tc04 | part02 | "input.txt"         | 5169198  |
