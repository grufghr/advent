Feature: AoC 2023 Day 14: Parabolic Reflector Dish

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 20 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 136      |
      | tc02 | part01 | "input.txt"         | 107430   |
      | tc03 | part02 | "input_example.txt" | 64       |
      | tc04 | part02 | "input.txt"         | 96317    |
