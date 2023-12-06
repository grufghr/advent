Feature: AoC 2021 Day 08: Seven Segment Search

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 452

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 1096964
