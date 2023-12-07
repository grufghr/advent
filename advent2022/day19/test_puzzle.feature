Feature: AoC 2022 Day 19: Not Enough Minerals

  Background: Regression testing
    Given AoC puzzle
     Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 33

  @slow
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 790

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 2604

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 7350
