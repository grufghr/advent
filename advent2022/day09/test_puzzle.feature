Feature: AoC 2022 Day 09: Rope Bridge

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 6175

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2578
