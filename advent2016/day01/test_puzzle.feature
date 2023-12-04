Feature: AoC 2016 Day 01: No Time for a Taxicab

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then expected answer = <expected>
    Examples:
        | example input    | expected |
        | "R2, L3"         | 5        |
        | "R2, R2, R2"     | 2        |
        | "R5, L5, R5, R3" | 12       |
        | "R8, R4, R4, R8" | 8        |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 242

  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then expected answer = <expected>
    Examples:
        | example input    | expected |
        | "R2, L3"         | None     |
        | "R2, R2, R2"     | None     |
        | "R5, L5, R5, R3" | None     |
        | "R8, R4, R4, R8" | 4        |

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 150
      And execution time < 1 secs
