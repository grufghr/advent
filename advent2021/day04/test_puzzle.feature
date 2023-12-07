Feature: AoC 2021 Day 04: Giant Squid

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 4512

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 64084

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 1924

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 12833
