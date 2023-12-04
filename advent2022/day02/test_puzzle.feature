Feature: AoC 2022 Day 02: Rock Paper Scissors

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 15

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 13682

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 12

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 12881
      And execution time < 1 secs
