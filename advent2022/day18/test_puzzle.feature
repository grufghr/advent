Feature: AoC 2022 Day 18: Boiling Boulders
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 64
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 3364

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 58

  @slow
  Scenario: part02 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 2006
      And execution time < 20 secs
