Feature: AoC 2022 Day 03: Rucksack Reorganization

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 157      |
      | tc02 | part01 | "input.txt"         | 8243     |
      | tc03 | part02 | "input_example.txt" | 70       |
      | tc04 | part02 | "input.txt"         | 2631     |
