Feature: AoC 2015 Day 04: The Ideal Stocking Stuffer

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 10 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 1048970  |
      | tc02 | part01 | "input.txt"         | 254575   |
      | tc03 | part02 | "input_example.txt" | 5714438  |
      | tc04 | part02 | "input.txt"         | 1038736  |
