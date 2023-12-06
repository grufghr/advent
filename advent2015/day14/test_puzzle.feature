Feature: AoC 2015 Day 14: Reindeer Olympics

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 1120

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 2696

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 689

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 1084
