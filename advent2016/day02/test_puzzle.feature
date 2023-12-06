Feature: AoC 2016 Day 02: Bathroom Security

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 12578

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 516DD
