Feature: AoC 2015 Day 11: Corporate Policy

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  @slow
  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part02
     Then expected answer = <expected>
    Examples:
        | example input | expected |
        | "abcdefgh"    | abcdffaa |
        | "ghijklmn"    | ghjaabcc |

  @slow
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = cqjxxyzz

# @skip('No examples for part02')
#  Scenario: part02 examples
#    Given example input in file "input_example.txt"
#     When solve part02
#     Then expected answer = TBC

  @slow
  Scenario: part02 (execution time ~5 secs)
    Given input "cqjxxyzz"
     When solve part02
     Then expected answer = cqkaabcc
      And execution time < 5 secs
