Feature: AoC 2021 Day 06: Lanternfish

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 380243

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 1708791884591