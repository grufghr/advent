Feature: AoC 2015 Day 10: Elves Look, Elves Say

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 82350    |
      | tc02 | part01 | "input.txt"         | 360154   |
      | tc03 | part02 | "input_example.txt" | 1166642  |
      | tc04 | part02 | "input.txt"         | 5103798  |
