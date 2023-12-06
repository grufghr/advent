Feature: AoC 2022 Day 02: Rock Paper Scissors

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 15

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 13682

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 12

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 12881
