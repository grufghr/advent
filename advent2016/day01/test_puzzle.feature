Feature: AoC 2016 Day 01: No Time for a Taxicab

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 242

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 150
