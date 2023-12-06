Feature: AoC 2023 Day 06: Wait For It

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 288

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 625968

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 71503

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 43663323
