Feature: AoC 2020 Day 01: Report Repair

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 514579

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1003971

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 241861950

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 84035952
