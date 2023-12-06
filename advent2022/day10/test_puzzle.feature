Feature: AoC 2022 Day 10: Cathode-Ray Tube

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 14360

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer is list
      """
      ["###...##..#..#..##..####.###..####.####.",
       "#..#.#..#.#.#..#..#.#....#..#.#.......#.",
       "###..#....##...#..#.###..#..#.###....#..",
       "#..#.#.##.#.#..####.#....###..#.....#...",
       "#..#.#..#.#.#..#..#.#....#.#..#....#....",
       "###...###.#..#.#..#.####.#..#.####.####.",
       "........................................"]
      """
