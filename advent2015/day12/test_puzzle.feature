Feature: AoC 2015 Day 12: JSAbacusFramework.io

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 33

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 111754

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 16

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 65402
