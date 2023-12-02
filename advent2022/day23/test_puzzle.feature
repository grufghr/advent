Feature: AoC 2022 Day 23: Unstable Diffusion
  
  Background: Regression testing
    Given advent 2022 day 23 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 110

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 4218

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 20

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 976
      And performance < 25 seconds
