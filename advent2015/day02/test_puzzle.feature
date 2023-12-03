Feature: AoC 2015 Day 02: I Was Told There Would Be No Math

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 101

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 1586300

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 48

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 3737498
      And execution time < 1 secs
