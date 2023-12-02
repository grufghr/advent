Feature: AoC 2022 Day 08: Treetop Tree House

  Background: Regression testing
    Given advent 2022 day 08 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 21

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 1796

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 8

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 288120
      And performance < 1 secs
