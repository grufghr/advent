Feature: AoC 2022 Day 21: Monkey Math
  
  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
      When solve part01
      Then expected answer = 21120928600114

  Scenario: part02
    Given input in file "input.txt"
      When solve part02
      Then expected answer = 3453748220116
  