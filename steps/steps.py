"""
Unit Test Scenario functions
"""
# general imports
from behave import *
import re
import json
import importlib


#
# Background
#


@given('AoC puzzle')
def step_given_aoc(context):
    regex_result = re.findall(r'(\d+)', context.feature.filename)
    context.year = regex_result[0]
    context.day = regex_result[1]
    puzzle_name = f'advent{context.year}.day{context.day}.puzzle'
    context.puzzle = importlib.import_module(puzzle_name)


@then('validate test feature name')
def step_validate_feature(context):
    regex_result = re.match(r'AoC (?P<year>\d+) Day (?P<day>\d+):', context.feature.name)
    result = regex_result.groupdict()
    assert context.year == result['year'], f'wrong year in feature name {context.feature.filename}'
    assert context.day == result['day'], f'wrong day in feature name {context.feature.filename}'


#
# Scenario
#
@given('input in file "{input_file}"')
def given_input_file(context, input_file):
    puzzle = context.puzzle
    context.input_data = puzzle.load_data(input_file)


@given('input "{input_data}"')
def given_input(context, input_data):
    context.input_data = input_data


@when('solve {part}')
def when_solve01(context, part):
    puzzle = context.puzzle
    input_data = context.input_data
    if part == 'part01':
        context.answer = puzzle.solve01(input_data)
    elif part == 'part02':
        context.answer = puzzle.solve02(input_data)
    else:
        raise Exception(f'unknown function {part}')


@then('expected answer = {expected}')
def then_answer(context, expected):
    if expected == 'None':
        expected = None

    if isinstance(context.answer, int):
        expected = int(expected)
    elif not isinstance(context.answer, str):
        print(f'answer is {type(context.answer)}')

    answer = context.answer
    assert type(answer) == type(expected), f'answer {type(answer)} != {type(expected)} (expected)'
    assert answer == expected, f'answer {answer} != {expected} (expected)'


@then('expected answer is list')
def step_expected_as_list(context):
    expected = json.loads(str(context.text))
    answer = context.answer
    assert type(answer) == type(expected), f'answer {type(answer)} != {type(expected)} (expected)'
    assert answer == expected, f'answer {answer} != {expected} (expected)'
