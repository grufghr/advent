Feature: AoC 2015 Day 12: JSAbacusFramework.io

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

#  @skip('no examples')
#  Scenario: part01 examples
#    Given example input in file "input_example.txt"
#     When solve part01
#     Then answer = TBC

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 111754

#  @skip('no examples')
#  Scenario: part02 examples
#    Given example input in file "input_example.txt"
#     When solve part02
#     Then answer = 982

  Scenario: part02 (execution time ~2 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 65402
      And execution time < 2 secs
