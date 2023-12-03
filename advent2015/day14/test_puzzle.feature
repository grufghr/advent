Feature: AoC 2015 Day 14: Reindeer Olympics

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01 with param 1000
     Then answer = 1120

  Scenario: part01
    Given input in file "input.txt"
     When solve part01 with param 2503
     Then answer = 2696

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02 with param 1000
     Then answer = 689

  Scenario: part02
    Given input in file "input.txt"
     When solve part02 with param 2503
     Then answer = 1084
      And execution time < 1 secs
