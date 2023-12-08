Feature: AoC 2022 Day 10: Cathode-Ray Tube

  Scenario Outline: solve puzzle
    Given AoC puzzle
      And input in file <filename>
     When solve <part>
     Then correct test feature name
      And expected answer = <expected>
      And execution time < 1 secs
    Examples:
      | name | part   | filename            | expected |
      | tc01 | part01 | "input_example.txt" | 13140    |
      | tc02 | part01 | "input.txt"         | 14360    |

  Scenario: solve puzzle example
    Given AoC puzzle
      And input in file "input_example.txt"
     When solve part02
     Then correct test feature name
      And expected answer is list
     """
     ["##..##..##..##..##..##..##..##..##..##..",
      "###...###...###...###...###...###...###.",
      "####....####....####....####....####....",
      "#####.....#####.....#####.....#####.....",
      "######......######......######......###.",
      "#######.......#######.......#######....#",
      "........................................"]
     """
      And execution time < 1 secs

  Scenario: solve puzzle
    Given AoC puzzle
      And input in file "input.txt"
     When solve part02
     Then correct test feature name
      And expected answer is list
      """
      ["###...##..#..#..##..####.###..####.####.",
       "#..#.#..#.#.#..#..#.#....#..#.#.......#.",
       "###..#....##...#..#.###..#..#.###....#..",
       "#..#.#.##.#.#..####.#....###..#.....#...",
       "#..#.#..#.#.#..#..#.#....#.#..#....#....",
       "###...###.#..#.#..#.####.#..#.####.####.",
       "........................................"]
      """
      And execution time < 1 secs
