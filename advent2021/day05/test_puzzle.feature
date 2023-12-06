Feature: AoC 2021 Day 05: Hydrothermal Venture

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 6666

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 19081