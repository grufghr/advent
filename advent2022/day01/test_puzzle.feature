Feature: AoC 2022 Day 01: Calorie Counting
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 24000
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 71124

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 45000

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 204639
      And execution time < 1 secs
