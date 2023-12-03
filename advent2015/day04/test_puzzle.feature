Feature: AoC 2015 Day 04: The Ideal Stocking Stuffer

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then answer = <answer>
    Examples:
        | example input | answer  |
        | "abcdef"      | 609043  |
        | "pqrstuv"     | 1048970 |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 254575

  @slow
  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then answer = <answer>
    Examples:
        | example input | answer  |
        | "abcdef"      | 6742839 |
        | "pqrstuv"     | 5714438 |

  @slow
  Scenario: part02 (execution time ~2 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 1038736
      And execution time < 2 secs
