Feature: AoC 2020 Day 01: Report Repair

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1003971

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 84035952
