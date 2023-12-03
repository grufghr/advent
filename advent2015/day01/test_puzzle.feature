Feature: AoC 2015 Day 01: Not Quite Lisp

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then answer = <answer>
    Examples:
        | example input    | answer |
        | "(())"           | 0      |
        | "()()"           | 0      |
        | "((("            | 3      |
        | "(()(()("        | 3      |
        | "))((((("        | 3      |
        | "())"            | -1     |
        | "))("            | -1     |
        | ")))"            | -3     |
        | ")())())"        | -3     |
        | ")"              | -1     |
        | "()())"          | -1     |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 280

  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then answer = <answer>
    Examples:
        | example input    | answer |
        | "(())"           | 0      |
        | "()()"           | 0      |
        | "((("            | 0      |
        | "(()(()("        | 0      |
        | "))((((("        | 1      |
        | "())"            | 3      |
        | "))("            | 1      |
        | ")))"            | 1      |
        | ")())())"        | 1      |
        | ")"              | 1      |
        | "()())"          | 5      |

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 1797
      And execution time < 1 secs
