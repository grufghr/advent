Feature: AoC 2022 Day 05: Supply Stacks

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected  |
      | tc01 | part01 | "input_example.txt" | CMZ       |
      | tc02 | part01 | "input.txt"         | FZCMJCRHZ |
      | tc03 | part02 | "input_example.txt" | MCD       |
      | tc04 | part02 | "input.txt"         | JSDHQMZGF |
