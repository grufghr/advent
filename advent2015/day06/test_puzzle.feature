Feature: AoC 2015 Day 06: Probably a Fire Hazard

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 998996

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 543903

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 1001996

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 14687245
      And execution time < 1 secs
