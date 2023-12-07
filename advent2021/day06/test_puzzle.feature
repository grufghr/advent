Feature: AoC 2021 Day 06: Lanternfish

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 5934

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 380243

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 26984457539

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 1708791884591
