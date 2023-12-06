Feature: AoC 2017 Day 03: Spiral Memory

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 371

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 369601
