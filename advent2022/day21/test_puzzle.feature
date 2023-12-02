Feature: AoC 2022 Day 21: Monkey Math
  
  Background: Regression testing
    Given advent 2022 day 21 puzzle

  Scenario Outline: part01 examples
    Given example input in file <example input file>
     When solve part01
     Then answer = <answer>
    Examples:
        | example input file    | answer |
        | "input_example01.txt" | 152    |
        | "input_example02.txt" | 34     |
        
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 21120928600114

  Scenario Outline: part02 examples
    Given example input in file <example input file>
     When solve part02
     Then answer = <answer>
    Examples:
        | example input file    | answer |
        | "input_example01.txt" | 301    |
        | "input_example02.txt" | 19     |
        
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 3453748220116
      And performance < 1 seconds
