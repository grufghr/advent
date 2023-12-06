Feature: AoC 2021 Day 25: Sea Cucumber

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  @slow
  Scenario: part01 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 532
