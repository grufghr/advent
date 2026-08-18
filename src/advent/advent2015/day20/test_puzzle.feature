Feature: AoC 2015 Day 20: Infinite Elves and Infinite Houses

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 30 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 210      |
      | tc02 | part01 | "input.txt"         | 665280   |
      | tc03 | part02 | "input_example.txt" | 168      |
      | tc04 | part02 | "input.txt"         | 705600   |
