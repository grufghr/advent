Feature: AoC 2023 Day 06: Wait For It

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: solve puzzle
    Given input in file <filename>
     When solve <part>
     Then expected answer = <expected>
    Examples:
      | part   | filename            | expected |
      | part01 | "input_example.txt" | 288      |
      | part01 | "input.txt"         | 625968   |
      | part02 | "input_example.txt" | 71503    |
      | part02 | "input.txt"         | 43663323 |
