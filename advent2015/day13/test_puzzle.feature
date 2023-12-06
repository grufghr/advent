Feature: AoC 2015 Day 13: Knights of the Dinner Table

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 330

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 664

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 286

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 640
