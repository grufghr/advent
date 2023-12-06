Feature: AoC 2022 Day 15: Beacon Exclusion Zone

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 5716881

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 10852583132904
