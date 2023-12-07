Feature: AoC 2022 Day 08: Treetop Tree House

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 21

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1796

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 8

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 288120
