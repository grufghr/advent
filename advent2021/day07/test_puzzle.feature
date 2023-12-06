Feature: AoC 2021 Day 07: The Treachery of Whales

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 323647

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 87640209
