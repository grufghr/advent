Feature: AoC 2019 Day 02: 1202 Program Alarm
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 100
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 5305097

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = None

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 4925
      And execution time < 1 secs
