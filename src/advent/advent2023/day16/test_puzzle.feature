Feature: AoC 2023 Day 16: The Floor Will Be Lava

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 35 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 46       |
      | tc02 | part01 | "input.txt"         | 6361     |
      | tc03 | part02 | "input_example.txt" | 51       |
      | tc04 | part02 | "input.txt"         | 6701     |
