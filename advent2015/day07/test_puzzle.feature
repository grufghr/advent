Feature: AoC 2015 Day 07: Some Assembly Required

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 65079

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 16076

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 65079

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2797
      And execution time < 1 secs
