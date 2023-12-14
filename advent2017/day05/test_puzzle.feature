Feature: AoC 2017 Day 05: A Maze of Twisty Trampolines, All Alike

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 15 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 5        |
      | tc02 | part01 | "input.txt"         | 378980   |
      | tc03 | part02 | "input_example.txt" | 10       |
      | tc04 | part02 | "input.txt"         | 26889114 |
