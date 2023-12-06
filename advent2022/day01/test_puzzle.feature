Feature: AoC 2022 Day 01: Calorie Counting

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 71124

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 204639
