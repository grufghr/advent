Feature: AoC 2023 Day 18: Lavaduct Lagoon

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected       |
      | tc01 | part01 | "input_example.txt" | 62             |
      | tc02 | part01 | "input.txt"         | 58550          |
      | tc03 | part02 | "input_example.txt" | 952408144115   |
      | tc04 | part02 | "input.txt"         | 47452118468566 |
