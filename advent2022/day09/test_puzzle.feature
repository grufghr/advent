Feature: AoC 2022 Day 09: Rope Bridge

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input in file <example input file>
     When solve part01
     Then expected answer = <expected>
    Examples:
        | example input file    | expected |
        | "input_example01.txt" | 13       |
        | "input_example02.txt" | 88       |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 6175

  Scenario Outline: part02 examples
    Given example input in file <example input file>
     When solve part02
     Then expected answer = <expected>
    Examples:
        | example input file    | expected |
        | "input_example01.txt" | 1        |
        | "input_example02.txt" | 36       |

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2578
      And execution time < 1 secs
