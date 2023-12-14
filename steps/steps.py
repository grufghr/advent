"""
Feature Test Scenario functions
"""
# general imports
from behave import given, when, then
import re
import json
import importlib
import time


@given('AoC puzzle')
def given_aoc(context):
    regex_result = re.findall(r'(\d+)', context.feature.filename)
    context.year = regex_result[0]
    context.day = regex_result[1]
    puzzle_name = f'advent{context.year}.day{context.day}.puzzle'
    context.puzzle = importlib.import_module(puzzle_name)


@given('input in file "{input_file}"')
def given_input_file(context, input_file):
    puzzle = context.puzzle
    context.input_data = puzzle.load_data(input_file)


@given('input "{input_data}"')
def given_input(context, input_data):
    context.input_data = input_data


@when('solve {funcname}')
def when_part01(context, funcname):
    func = getattr(context.puzzle, funcname)
    # will raise AttributeError if function not found

    ts = time.time()
    # call function
    context.answer = func(context.input_data)
    context.time = time.time() - ts


@then('test feature name is correct')
def then_validate_feature(context):
    regex_result = re.match(r'AoC (?P<year>\d+) Day (?P<day>\d+):', context.feature.name)
    result = regex_result.groupdict()
    assert context.year == result['year'], f'wrong year in feature name {context.feature.filename}'
    assert context.day == result['day'], f'wrong day in feature name {context.feature.filename}'


@then('expected answer = {expected}')
def then_expected_answer(context, expected):
    if expected == 'None':
        expected = None

    if isinstance(context.answer, int):
        expected = int(expected)
    elif not isinstance(context.answer, str):
        print(f'answer is {type(context.answer)}')

    validate_expected(context, expected)


@then('expected answer is list')
def then_expected_is_list(context):
    expected = json.loads(str(context.text))
    validate_expected(context, expected)


def validate_expected(context, expected):
    answer = context.answer
    assert type(answer) == type(expected), f'answer {type(answer)} != {type(expected)} (expected)'
    assert answer == expected, f'answer {answer} != {expected} (expected)'


@then('execution time < {time} secs')
def then_execution_time(context, time):
    if 'slow' not in context.tags:
        assert context.time < float(time), f'puzzle took {context.time} secs'
