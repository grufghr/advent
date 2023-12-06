Feature: AoC 2015 Day 12: JSAbacusFramework.io

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 111754

  Scenario: part02 (execution time ~2 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 65402
