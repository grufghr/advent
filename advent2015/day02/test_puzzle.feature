Feature: AoC 2015 Day 02: I Was Told There Would Be No Math

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 101

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1586300

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 48

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 3737498
