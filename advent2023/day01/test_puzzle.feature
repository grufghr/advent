Feature: AoC 2023 Day 01: Trebuchet?!
  
  Background: Regression testing
    Given advent 2023 day 01 puzzle

  Scenario: part01 examples
    Given example input in file "input_example01.txt"
     When solve part01
     Then answer = 142

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 54239

  Scenario: part02 examples
    Given example input in file "input_example02.txt"
     When solve part02
     Then answer = 281

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 55343
      And performance < 1 secs