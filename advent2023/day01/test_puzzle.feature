Feature: AoC 2023 Day 01: Trebuchet?!

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example_01.txt"
     When solve part01
     Then expected part01 answer = 142

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 54239

  Scenario: part02 example
    Given input in file "input_example_02.txt"
     When solve part02
     Then expected part02 answer = 281

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 55343
