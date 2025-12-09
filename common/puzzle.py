"""
Advent of Code 2023 Day nn: Puzzle Name
"""
import os


def part01(input_data):
    print(input_data)
    return 'tbc'


def part02(input_data):
    return 'tbc'


def parse_data(input_data):
    data = []
    for line_text in input_data.splitlines():
        data.append(line_text)
    return data


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input_example.txt')

    answer01 = part01(input_data)
    print(f'part01 answer = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 answer = {answer02}')
