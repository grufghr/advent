Feature: AoC 2019 Day 02: 1202 Program Alarm

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 5305097

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 4925
