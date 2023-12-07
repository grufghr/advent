Feature: AoC 2021 Day 07: The Treachery of Whales

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 37

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 323647

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 168

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 87640209
