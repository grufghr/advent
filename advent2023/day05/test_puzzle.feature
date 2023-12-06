Feature: AoC 2023 Day 05: If You Give A Seed A Fertilizer

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 227653707

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 78775051
