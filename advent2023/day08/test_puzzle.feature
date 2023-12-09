Feature: AoC 2023 Day 08: Haunted Wasteland

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected       |
      | tc01 | part01 | "input_example.txt" | 2              |
      | tc02 | part01 | "input.txt"         | 16697          |
      | tc03 | part02 | "input_example.txt" | 2              |
      | tc04 | part02 | "input.txt"         | 10668805667831 |
