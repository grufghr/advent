Feature: AoC 2018 Day 01: Chronal Calibration

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 599

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 81204
