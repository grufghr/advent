Feature: AoC 2022 Day 07: No Space Left On Device

  Background: Regression testing
    Given advent 2022 day 07 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 95437

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 1513699

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 24933642

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 7991939
      And performance < 1 secs
