Feature: AoC 2017 Day 05: A Maze of Twisty Trampolines, All Alike

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 378980

  @slow
  Scenario: part02 (execution time ~10 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 26889114
