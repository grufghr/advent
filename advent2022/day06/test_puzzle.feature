Feature: AoC 2022 Day 06: Tuning Trouble

  Background: Regression testing
    Given advent 2022 day 06 puzzle

  Scenario Outline: part01 examples
    Given example input <example input>
     When solve part01
     Then answer = <answer>
    Examples: 
        | example input                       | answer |
        | "mjqjpqmgbljsphdztnvjfqwrcgsmlb"    | 7      |
        | "bvwbjplbgvbhsrlpgdmjqwftvncz"      | 5      |
        | "nppdvjthqldpwncqszvftbrmjlhg"      | 6      |
        | "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" | 10     |
        | "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  | 11     |

  Scenario: part01
    Given input in file "input.txt"
      When solve part01
      Then answer = 1531

  Scenario Outline: part02 examples
    Given example input <example input>
     When solve part02
     Then answer = <answer>
    Examples: 
        | example input                       | answer |
        | "mjqjpqmgbljsphdztnvjfqwrcgsmlb"    | 19     |
        | "bvwbjplbgvbhsrlpgdmjqwftvncz"      | 23     |
        | "nppdvjthqldpwncqszvftbrmjlhg"      | 23     |
        | "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" | 29     |
        | "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  | 26     |

  Scenario: part02
    Given input in file "input.txt"
      When solve part02
      Then answer = 2518
        And performance < 1 seconds
