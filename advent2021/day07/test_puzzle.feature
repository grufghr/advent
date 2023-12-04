Feature: AoC 2021 Day 07: The Treachery of Whales
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 37
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 323647

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 168

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 87640209
      And execution time < 1 secs
