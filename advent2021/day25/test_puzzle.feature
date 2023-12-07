Feature: AoC 2021 Day 25: Sea Cucumber

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 58

  @slow
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 532
