Feature: AoC 2022 Day 11: Monkey in the Middle

  Background: Regression testing
    Given advent 2022 day 11 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 10605

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 56595

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 2713310158

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 15693274740
      And performance < 1 secs
