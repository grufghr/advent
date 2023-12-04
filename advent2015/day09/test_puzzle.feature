Feature: AoC 2015 Day 09: All in a Single Night

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 605

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 117

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 982

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 909
      And execution time < 1 secs
