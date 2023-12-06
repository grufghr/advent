Feature: AoC 2022 Day 06: Tuning Trouble

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1531

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2518
