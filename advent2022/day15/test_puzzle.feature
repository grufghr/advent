Feature: AoC 2022 Day 15: Beacon Exclusion Zone

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected       |
      | tc01 | part01 | "input_example.txt" | 26             |
      | tc02 | part01 | "input.txt"         | 5716881        |
      | tc03 | part02 | "input_example.txt" | 56000011       |
      | tc04 | part02 | "input.txt"         | 10852583132904 |
