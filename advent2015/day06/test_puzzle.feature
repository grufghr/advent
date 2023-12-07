Feature: AoC 2015 Day 06: Probably a Fire Hazard

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 998996   |
      | tc02 | part01 | "input.txt"         | 543903   |
      | tc03 | part02 | "input_example.txt" | 1001996  |
      | tc04 | part02 | "input.txt"         | 14687245 |
