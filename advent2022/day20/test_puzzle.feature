Feature: AoC 2022 Day 20: Grove Positioning System

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 3

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 7153

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 1623178306

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 6146976244822
