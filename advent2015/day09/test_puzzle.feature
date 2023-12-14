Feature: AoC 2015 Day 09: All in a Single Night

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 605      |
      | tc02 | part01 | "input.txt"         | 117      |
      | tc03 | part02 | "input_example.txt" | 982      |
      | tc04 | part02 | "input.txt"         | 909      |
