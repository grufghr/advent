Feature: AoC 2022 Day 02: Rock Paper Scissors

  Background: Regression testing
    Given advent 2022 day 02 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 15

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 13682

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 12

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 12881
      And performance < 1 seconds
