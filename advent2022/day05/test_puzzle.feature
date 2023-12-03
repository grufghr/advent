Feature: AoC 2022 Day 05: Supply Stacks

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = CMZ

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = FZCMJCRHZ

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = MCD

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = JSDHQMZGF
      And execution time < 1 secs
