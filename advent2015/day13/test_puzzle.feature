Feature: AoC 2015 Day 13: Knights of the Dinner Table

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 330

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 664

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 286

  @slow
  Scenario: part02 (execution time ~2 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 640
      And execution time < 2 secs
