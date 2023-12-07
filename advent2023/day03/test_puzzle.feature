Feature: AoC 2023 Day 03: Gear Ratios

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 4361

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 520019

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 467835

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 75519888
