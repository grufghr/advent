Feature: AoC 2022 Day 18: Boiling Boulders

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 3364

  @slow
  Scenario: part02 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2006
