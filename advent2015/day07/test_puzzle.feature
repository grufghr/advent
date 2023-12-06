Feature: AoC 2015 Day 07: Some Assembly Required

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 65079

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 16076

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 65079

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 2797
