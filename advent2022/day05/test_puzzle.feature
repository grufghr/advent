Feature: AoC 2022 Day 05: Supply Stacks

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = CMZ

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = FZCMJCRHZ

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = MCD

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = JSDHQMZGF
