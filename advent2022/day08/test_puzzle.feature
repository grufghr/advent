Feature: AoC 2022 Day 08: Treetop Tree House

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 21

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1796

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 8

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 288120
      And execution time < 1 secs
