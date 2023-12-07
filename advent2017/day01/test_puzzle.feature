Feature: AoC 2017 Day 01: Inverse Captcha

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 9

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1047

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 6

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 982
