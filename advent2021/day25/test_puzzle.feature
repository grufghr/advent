Feature: AoC 2021 Day 25: Sea Cucumber
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 58
  
  @slow
  Scenario: part01 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part01
     Then answer = 532
      And execution time < 20 secs

