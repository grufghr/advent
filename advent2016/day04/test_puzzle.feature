Feature: AoC 2016 Day 04: Security Through Obscurity

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 2181

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 245102

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 324

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 324
