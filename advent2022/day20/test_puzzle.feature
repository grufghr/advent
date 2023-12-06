Feature: AoC 2022 Day 20: Grove Positioning System

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 7153

  @slow
  Scenario: part02 (execution time ~15 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 6146976244822
