Feature: AoC 2021 Day 03: Binary Diagnostic
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 198
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1071734

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 230

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 6124992
      And execution time < 1 secs
