"""
Advent of Code - Code Analysis
"""

import sys
import argparse
import importlib
import cProfile
import pstats
from pathlib import Path


def _get_arguments():
    parser = argparse.ArgumentParser(description='Performance analyzer using cProfile.')
    parser.add_argument(
        'year',
        type=int,
        help='Puzzle year',
    )
    parser.add_argument(
        'day',
        type=int,
        help='Puzzle year',
    )
    parser.add_argument(
        'function_name',
        type=str,
        nargs='?',  # optional
        default='part02',
        help='function to be tested (default = part02)',
    )
    parser.add_argument(
        'input_datafile',
        type=str,
        nargs='?',  # optional
        default='input.txt',
        help='input datafile (default = input.txt)',
    )

    return parser.parse_args()


def main():
    args = _get_arguments()

    # Identify module
    module_str = f'advent.advent{args.year}.day{args.day:0>2}.puzzle'
    try:
        target_module = importlib.import_module(module_str)
    except ModuleNotFoundError as e:
        print(f"Error: Could not import module '{module_str}'.")
        print(f'Details: {e}')
        sys.exit(1)

    # Retrieve function
    if not hasattr(target_module, args.function_name):
        print(f"Error: Function '{args.function_name}' not found in '{module_str}'.")
        sys.exit(1)
    target_function = getattr(target_module, args.function_name)

    # Load input data
    module_dir = Path(target_module.__file__).resolve().parent
    input_datafile = module_dir / args.input_datafile

    if not input_datafile.exists():
        print(f"Error: Input file not found at '{input_datafile.resolve()}'")
        sys.exit(1)

    load_data_function = target_module.load_data
    input_data = load_data_function(input_datafile)

    # Performance Analaysis
    profiler = cProfile.Profile()
    profiler.enable()

    # ... do something ...
    answer = target_function(input_data)

    profiler.disable()

    print(f'{target_function} {answer=}')

    # display stats
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats(pstats.SortKey.CUMULATIVE)
    stats.print_stats()


if __name__ == '__main__':
    main()

