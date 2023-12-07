Feature: AoC 2023 Day 05: If You Give A Seed A Fertilizer

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 35

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 227653707

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 46

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 78775051
