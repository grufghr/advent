Feature: AoC 2021 Day 13: Transparent Origami
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01 with variable length args
     Then answer = 17
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01 with variable length args
     Then answer = 664

  Scenario: part02 examples
    Given example input in file "input_example.txt"
      And expected answer is list
      """
      [
        "#####",
        "#...#",
        "#...#",
        "#...#",
        "#####"
        ]
      """
     When solve part02 with variable length args
     Then answer matches expected

  Scenario: part02
    Given input in file "input.txt"
      And expected answer is list
      """
      [
        "####.####...##.#..#.####.#....###..#...",
        "#....#.......#.#.#.....#.#....#..#.#...",
        "###..###.....#.##.....#..#....###..#...",
        "#....#.......#.#.#...#...#....#..#.#...",
        "#....#....#..#.#.#..#....#....#..#.#...",
        "####.#.....##..#..#.####.####.###..####"
        ]
      """
     When solve part02 with variable length args
     Then answer matches expected
      And execution time < 1 secs
