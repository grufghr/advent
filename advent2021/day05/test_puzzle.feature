Feature: AoC 2021 Day 05: Hydrothermal Venture
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 5
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 6666

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 12

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 19081
      And execution time < 1 secs
