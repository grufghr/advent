Feature: AoC 2016 Day 04: Security Through Obscurity

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 2181

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 245102

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 324

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 324
      And execution time < 1 secs
