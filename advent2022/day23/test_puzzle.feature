Feature: AoC 2022 Day 23: Unstable Diffusion
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name
     
  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 110

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 4218

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 20

  @slow
  Scenario: part02 (execution time ~25 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 976
      And execution time < 25 secs
