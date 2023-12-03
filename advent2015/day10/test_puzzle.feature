Feature: AoC 2015 Day 10: Elves Look, Elves Say

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 82350

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 360154

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 1166642

  @slow
  Scenario: part02 (execution time ~7 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 5103798
      And execution time < 7 secs
