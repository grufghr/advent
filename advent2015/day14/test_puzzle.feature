Feature: AoC 2015 Day 14: Reindeer Olympics

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 2696

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 1084
