Feature: AoC 2023 Day 03: Gear Ratios

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 520019

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 75519888
