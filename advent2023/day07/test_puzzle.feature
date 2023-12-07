Feature: AoC 2023 Day 07: Camel Cards

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected  |
      | tc01 | part01 | "input_example.txt" | 6440      |
      | tc02 | part01 | "input.txt"         | 250232501 |
      | tc03 | part02 | "input_example.txt" | 5905      |
      | tc04 | part02 | "input.txt"         | 249138943 |
