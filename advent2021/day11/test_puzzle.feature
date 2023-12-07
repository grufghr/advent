Feature: AoC 2021 Day 11: Dumbo Octopus

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 1656

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1637

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 195

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 242
