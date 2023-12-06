Feature: AoC 2015 Day 04: The Ideal Stocking Stuffer

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 1048970

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 254575

  @slow
  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 5714438

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 1038736
