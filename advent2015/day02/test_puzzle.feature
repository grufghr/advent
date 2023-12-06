Feature: AoC 2015 Day 02: I Was Told There Would Be No Math

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1586300

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 3737498
