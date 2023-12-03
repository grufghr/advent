Feature: AoC 2022 Day 10: Cathode-Ray Tube

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 13140

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 14360

#  @skip('unittest, complex answer')
#  Scenario: part02 examples
#    Given example input in file "input_example.txt"
#     When solve part02
#     Then answer = "TBC"

#  @skip('unittest, complex answer')
#  Scenario: part02
#    Given input in file "input.txt"
#     When solve part02
#     Then answer = "TBC"
#      And execution time < 1 secs
