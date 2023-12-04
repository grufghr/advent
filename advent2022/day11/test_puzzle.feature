Feature: AoC 2022 Day 11: Monkey in the Middle

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 10605

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 56595

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 2713310158

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 15693274740
      And execution time < 1 secs
