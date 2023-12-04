Feature: AoC 2021 Day 11: Dumbo Octopus
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 1656
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1637

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 195

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 242
      And execution time < 1 secs
