Feature: AoC 2017 Day 02: Corruption Checksum
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example01.txt"
     When solve part01
     Then expected answer = 18
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 58975

  Scenario: part02 examples
    Given example input in file "input_example02.txt"
     When solve part02
     Then expected answer = 9

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 308
      And execution time < 1 secs
