Feature: AoC 2021 Day 13: Transparent Origami

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 17

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 664

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer is list
      """
      ["#####",
       "#...#",
       "#...#",
       "#...#",
       "#####"]
      """

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer is list
      """
      ["####.####...##.#..#.####.#....###..#...",
       "#....#.......#.#.#.....#.#....#..#.#...",
       "###..###.....#.##.....#..#....###..#...",
       "#....#.......#.#.#...#...#....#..#.#...",
       "#....#....#..#.#.#..#....#....#..#.#...",
       "####.#.....##..#..#.####.####.###..####"]
      """
