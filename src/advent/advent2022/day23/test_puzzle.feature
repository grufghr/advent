Feature: AoC 2022 Day 23: Unstable Diffusion

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 20 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 110      |
      | tc02 | part01 | "input.txt"         | 4218     |
      | tc03 | part02 | "input_example.txt" | 20       |
      | tc04 | part02 | "input.txt"         | 976      |
