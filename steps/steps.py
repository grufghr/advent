"""
Unit Test Scenario functions
"""
# general imports
from behave import *
import importlib
import time


@given('advent {year} day {day} puzzle')
def step_impl(context, year, day):
    puzzle_name = f'advent{year}.day{day}.puzzle'
    context.puzzle = importlib.import_module(puzzle_name)


@given('example input in file "{input_file}"')
def given_example_input_file(context, input_file):
    puzzle = context.puzzle
    context.input_data = puzzle.load_data(input_file)


@given('example input "{input_data}"')
def given_example_input(context, input_data):
    context.input_data = input_data


@given('input in file "{input_file}"')
def given_input(context, input_file):
    puzzle = context.puzzle
    context.input_data = puzzle.load_data(input_file)


@when('solve part01')
def when_solve01(context):
    puzzle = context.puzzle
    input_data = context.input_data
    context.answer = str(puzzle.solve01(input_data))


@when('solve part02')
def step_impl(context):
    puzzle = context.puzzle
    input_data = context.input_data
    ts = time.time()
    context.answer = str(puzzle.solve02(input_data))
    context.time = time.time() - ts


@then('answer = {answer}')
def then_solve01(context, answer):
    assert context.answer == answer, f'calculated answer {context.answer} != {answer}'


@then('performance < {time} seconds')
def then_performance(context, time):
    assert context.time < float(time), f'puzzle took {time} seconds'
