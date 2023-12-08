Feature: AoC 2023 Day 04: Scratchcards

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 25 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 13       |
      | tc02 | part01 | "input.txt"         | 23028    |
      | tc03 | part02 | "input_example.txt" | 30       |
      | tc04 | part02 | "input.txt"         | 9236992  |
