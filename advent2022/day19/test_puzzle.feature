Feature: AoC 2022 Day 19: Not Enough Minerals
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 33
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 790

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 2604

  @slow
  Scenario: part02 (execution time ~5 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 7350
      And execution time < 5 secs
