Feature: AoC 2022 Day 01: Calorie Counting
  
  Background: Regression testing
    Given advent 2022 day 01 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 24000
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 71124

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 45000

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 204639
      And performance < 1 secs
