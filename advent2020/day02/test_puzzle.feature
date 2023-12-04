Feature: AoC 2020 Day 02: Password Philosophy
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 2
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 410

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 1

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 694
      And execution time < 1 secs
