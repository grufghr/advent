Feature: AoC 2023 Day 04: Scratchcards

  Background: Regression testing
    Given AoC puzzle
     Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 13

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 23028

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 30

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 9236992
