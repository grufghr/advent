Feature: AoC 2022 Day 10: Cathode-Ray Tube

  Background: Regression testing
    Given advent 2022 day 10 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 13140

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 14360

#  @skip
#  Scenario: part02 examples
#    """
#      use unittest, complex answer
#    """
#    Given example input in file "input_example.txt"
#     When solve part02
#     Then answer = "TBC"

# @skip
#  Scenario: part02
#    """
#      use unittest, complex answer
#    """
#    Given input in file "input.txt"
#     When solve part02
#     Then answer = "TBC"
#      And performance < 1 secs
