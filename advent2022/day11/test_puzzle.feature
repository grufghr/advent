Feature: AoC 2022 Day 11: Monkey in the Middle

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 10605

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 56595

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 2713310158

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 15693274740
