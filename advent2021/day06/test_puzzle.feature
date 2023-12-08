Feature: AoC 2021 Day 06: Lanternfish

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected      |
      | tc01 | part01 | "input_example.txt" | 5934          |
      | tc02 | part01 | "input.txt"         | 380243        |
      | tc03 | part02 | "input_example.txt" | 26984457539   |
      | tc04 | part02 | "input.txt"         | 1708791884591 |
