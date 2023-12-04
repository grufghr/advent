Feature: AoC 2017 Day 01: Inverse Captcha
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then expected answer = <expected>
    Examples: 
        | example input | expected |
        | "1122"        | 3        |
        | "1111"        | 4        |
        | "1234"        | 0        |
        | "91212129"    | 9        |
        | "1212"        | 0        |
        | "1221"        | 3        |
        | "123425"      | 0        |
        | "123123"      | 0        |
        | "12131415"    | 0        |

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1047

  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then expected answer = <expected>
    Examples: 
        | example input | expected |
        | "1122"        | 0        |
        | "1111"        | 4        |
        | "1234"        | 0        |
        | "91212129"    | 6        |
        | "1212"        | 6        |
        | "1221"        | 0        |
        | "123425"      | 4        |
        | "123123"      | 12       |
        | "12131415"    | 4        |

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 982
      And execution time < 1 secs
