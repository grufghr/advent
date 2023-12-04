Feature: AoC 2015 Day 03: Perfectly Spherical Houses in a Vacuum

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then expected answer = <expected>
    Examples:
        | example input | expected |
        | ">"           | 2        |
        | "^>v<"        | 4        |
        | "^v^v^v^v^v"  | 2        |
        | "^v"          | 2        |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 2081

  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then expected answer = <expected>
    Examples:
        | example input | expected |
        | ">"           | 2        |
        | "^>v<"        | 3        |
        | "^v^v^v^v^v"  | 11       |
        | "^v"          | 3        |

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2341
      And execution time < 1 secs
