Feature: AoC 2017 Day 03: Spiral Memory
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then answer = <answer>
    Examples: 
        | example input | answer |
        | "1"           | 0      |
        | "12"          | 3      |
        | "23"          | 2      |
        | "1024"        | 31     |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 371

  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then answer = <answer>
    Examples: 
        | example input | answer |
        | "1"           | 2      |
        | "12"          | 23     |
        | "23"          | 25     |
        | "1024"        | 1968   |

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 369601
      And execution time < 1 secs
