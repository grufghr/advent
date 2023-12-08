Feature: AoC 2022 Day 21: Monkey Math
  
  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename              | expected       |
      | tc01 | part01 | "input_example.txt"   | 34             |
      | tc02 | part01 | "input.txt"           | 21120928600114 |
      | tc03 | part02 | "input_example.txt"   | 19             |
      | tc04 | part02 | "input.txt"           | 3453748220116  |

      | tc05 | part01 | "input_example01.txt" | 152            |
      | tc06 | part02 | "input_example01.txt" | 301            |
  