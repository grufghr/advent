Feature: AoC 2015 Day 06: Probably a Fire Hazard

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 998996

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 543903

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 1001996

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 14687245
