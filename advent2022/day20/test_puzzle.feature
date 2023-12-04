Feature: AoC 2022 Day 20: Grove Positioning System
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 3
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 7153

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 1623178306

  @slow
  Scenario: part02 (execution time ~15 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 6146976244822
      And execution time < 15 secs
