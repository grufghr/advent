Feature: AoC 2017 Day 05: A Maze of Twisty Trampolines, All Alike

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 5

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 378980

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 10

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 26889114
