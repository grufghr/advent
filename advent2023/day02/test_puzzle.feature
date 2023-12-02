Feature: AoC 2022 Day 02: Cube Conundrum

  Background: Regression testing
    Given advent 2023 day 02 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 8

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 2716

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 2286

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 72227
      And performance < 1 secs
