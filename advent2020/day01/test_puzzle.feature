Feature: AoC 2020 Day 01: Report Repair

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected  |
      | tc01 | part01 | "input_example.txt" | 514579    |
      | tc02 | part01 | "input.txt"         | 1003971   |
      | tc03 | part02 | "input_example.txt" | 241861950 |
      | tc04 | part02 | "input.txt"         | 84035952  |
