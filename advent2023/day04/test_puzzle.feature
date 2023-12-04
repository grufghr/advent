Feature: AoC 2023 Day 04: Scratchcards

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 13

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 23028

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 30

  @slow
  Scenario: part02 (execution time ~30 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 9236992
      And execution time < 30 secs
