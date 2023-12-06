Feature: AoC 2022 Day 15: Beacon Exclusion Zone

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 26

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 5716881

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 56000011

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 10852583132904
