Feature: AoC 2020 Day 01: Report Repair
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 514579
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 1003971

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 241861950

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 84035952
      And execution time < 1 secs
