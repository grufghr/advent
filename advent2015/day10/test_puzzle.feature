Feature: AoC 2015 Day 10: Elves Look, Elves Say

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 82350

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 360154

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 1166642

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 5103798
