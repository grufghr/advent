Feature: AoC 2021 Day 13: Transparent Origami

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then test feature name is correct
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 17       |
      | tc02 | part01 | "input.txt"         | 664      |

  Scenario: solve puzzle example
    Given AoC puzzle
      And input in file "input_example.txt"
     When solve part02
     Then test feature name is correct
      And expected answer is list
      """
      ["#####",
       "#...#",
       "#...#",
       "#...#",
       "#####"]
      """
      And execution time < 1 secs

  Scenario: solve puzzle
    Given AoC puzzle
      And input in file "input.txt"
     When solve part02
     Then test feature name is correct
      And expected answer is list
      """
      ["####.####...##.#..#.####.#....###..#...",
       "#....#.......#.#.#.....#.#....#..#.#...",
       "###..###.....#.##.....#..#....###..#...",
       "#....#.......#.#.#...#...#....#..#.#...",
       "#....#....#..#.#.#..#....#....#..#.#...",
       "####.#.....##..#..#.####.####.###..####"]
      """
      And execution time < 1 secs
