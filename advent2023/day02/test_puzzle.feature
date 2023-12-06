Feature: AoC 2023 Day 02: Cube Conundrum

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 2716

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 72227
