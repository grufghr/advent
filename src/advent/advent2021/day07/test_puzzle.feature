Feature: AoC 2021 Day 07: The Treachery of Whales

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 5 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 37       |
      | tc02 | part01 | "input.txt"         | 323647   |
      | tc03 | part02 | "input_example.txt" | 168      |
      | tc04 | part02 | "input.txt"         | 87640209 |
