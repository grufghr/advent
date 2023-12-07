Feature: AoC 2022 Day 07: No Space Left On Device

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 95437

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1513699

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 24933642

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 7991939
