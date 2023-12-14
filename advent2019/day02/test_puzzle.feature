Feature: AoC 2019 Day 02: 1202 Program Alarm

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 100      |
      | tc02 | part01 | "input.txt"         | 5305097  |
      | tc03 | part02 | "input_example.txt" | None     |
      | tc04 | part02 | "input.txt"         | 4925     |
