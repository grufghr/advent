Feature: AoC 2022 Day 10: Cathode-Ray Tube

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 13140

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 14360

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer is list
     """
     ["##..##..##..##..##..##..##..##..##..##..",
      "###...###...###...###...###...###...###.",
      "####....####....####....####....####....",
      "#####.....#####.....#####.....#####.....",
      "######......######......######......###.",
      "#######.......#######.......#######....#",
      "........................................"]
     """

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer is list
      """
      ["###...##..#..#..##..####.###..####.####.",
       "#..#.#..#.#.#..#..#.#....#..#.#.......#.",
       "###..#....##...#..#.###..#..#.###....#..",
       "#..#.#.##.#.#..####.#....###..#.....#...",
       "#..#.#..#.#.#..#..#.#....#.#..#....#....",
       "###...###.#..#.#..#.####.#..#.####.####.",
       "........................................"]
      """
