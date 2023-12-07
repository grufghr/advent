Feature: AoC 2019 Day 02: 1202 Program Alarm

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 100

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 5305097

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = None

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 4925
