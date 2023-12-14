Feature: AoC 2022 Day 20: Grove Positioning System

  @slow
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 15 secs
    Examples:
      | name | part   | filename            | expected      |
      | tc01 | part01 | "input_example.txt" | 3             |
      | tc02 | part01 | "input.txt"         | 7153          |
      | tc03 | part02 | "input_example.txt" | 1623178306    |
      | tc04 | part02 | "input.txt"         | 6146976244822 |
