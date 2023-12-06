Feature: AoC 2015 Day 04: The Ideal Stocking Stuffer

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 254575

  @slow
  Scenario: part02 (execution time ~2 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 1038736
