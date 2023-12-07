Feature: AoC 2023 Day 02: Cube Conundrum

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 8

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 2716

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 2286

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 72227
