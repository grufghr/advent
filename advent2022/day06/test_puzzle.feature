Feature: AoC 2022 Day 06: Tuning Trouble

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 6

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1531

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 23

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 2518
