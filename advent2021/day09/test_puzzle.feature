Feature: AoC 2021 Day 09: Smoke Basin
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 15
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 518

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 1134

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 949905
      And execution time < 1 secs
