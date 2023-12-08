#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 19: Not Enough Minerals
"""
import os
import re
import math
from collections import deque, defaultdict


LINE_BLUEPRINT_REGEX = re.compile(r'Blueprint (\d+): (.*)')

LINE_ROBOT_REGEX = re.compile(r'Each ([a-z]*) robot costs (\d+) ([a-z]*)(?: and (\d+) ([a-z]*))?.')


class RobotFactoryState:
    # record best geode collection over time for state
    # Note: class variable - so same dict for every state
    best_geodes = defaultdict(int)

    def __init__(self, blueprint):
        self.blueprint = blueprint

        # calculate maximum robots required for each type
        self.robot_max = {m: 0 for m in self.blueprint.keys()}
        self.robot_max['geode'] = math.inf  # geode most valuable (infinite)
        for robot_type, costs in self.blueprint.items():
            for mineral, qty in costs.items():
                self.robot_max[mineral] = max(self.robot_max[mineral], qty)

        # init state variables
        self.t = 0
        # init robot fleet with 1 ore collector
        self.robots = {m: 0 for m in blueprint.keys()}
        self.robots['ore'] = 1
        # init resources collected (with collect = 0)
        self.resources = {m: 0 for m in blueprint.keys()}

    def __repr__(self):
        return f'{self.t} {self.robots} {self.resources}'

    def reinitiliase(self):
        # reset class variables
        for t, bg in self.best_geodes.items():
            self.best_geodes[t] = 0

    def calc_best_geodes(self):
        a = self.best_geodes[self.t]
        b = self.resources['geode']
        self.best_geodes[self.t] = max(a, b)

    def continue_search(self, depth):
        # prune if more geodes produced by another state
        not_pruned = self.best_geodes[self.t] == self.resources['geode']
        return (self.t <= depth) and not_pruned

    def max_robots_built(self, robot_type):
        return self.robots[robot_type] + 1 > self.robot_max[robot_type]

    def get_next_state_options(self):
        # return all list of robots that can be built with available resources
        # available resources
        # -> list('mineral')
        state_list = [False]  # add false to start to do harvest
        for mineral, cost_list in self.blueprint.items():
            if all(qty <= self.resources[mineral_c] for mineral_c, qty in cost_list.items()):
                state_list.append(mineral)
        # prune
        if 'geode' in state_list:
            return ['geode']
        return state_list

    def build_robot(self, robot_type):
        self.robots[robot_type] += 1
        for mineral, qty in self.blueprint[robot_type].items():
            self.resources[mineral] -= qty

    def collect_resources(self):
        for robot_type, fleet in self.robots.items():
            self.resources[robot_type] += fleet

    def next_state(self):
        state = RobotFactoryState(self.blueprint)
        state.t = self.t + 1
        state.robots = self.robots.copy()
        state.resources = self.resources.copy()
        return state


def best_geodes(blueprint, end_cycle):
    state = RobotFactoryState(blueprint)
    state.reinitiliase()

    # initiate queue
    q = deque()
    q.append((state, set()))

    while q:
        state, skip_build = q.pop()

        state.calc_best_geodes()

        if state.continue_search(end_cycle):
            state_options = state.get_next_state_options()

            for robot_type in state_options:
                if not robot_type:
                    state_n = state.next_state()
                    state_n.collect_resources()
                    q.append((state_n, state_options))
                elif robot_type in skip_build:
                    # prune search if skipped build in last iteration
                    continue
                elif state.max_robots_built(robot_type):
                    # prune search if maximum robot_type built
                    continue
                else:
                    state_n = state.next_state()
                    state_n.collect_resources()
                    state_n.build_robot(robot_type)
                    q.insert(0, (state_n, set()))

    return state.best_geodes[end_cycle]


def part01(input_data):
    blueprints_map = input_data

    minutes = 24

    blueprint_quality_list = []
    for idx, blueprint in blueprints_map.items():
        blueprint_best = best_geodes(blueprint, minutes)
        blueprint_quality = idx * blueprint_best
        blueprint_quality_list.append(blueprint_quality)

    quality_sum = sum(blueprint_quality_list)

    return quality_sum


def part02(input_data):
    blueprints_map = input_data

    minutes = 32

    blueprints_first3 = list(blueprints_map.values())[:3]

    quality_first_n = 1
    for blueprint in blueprints_first3:
        blueprint_best = best_geodes(blueprint, minutes)
        quality_first_n = quality_first_n * blueprint_best

    return quality_first_n


def parse_data(input_data):
    blueprints_map = {}
    for blueprint_line in input_data.splitlines():
        match_b = LINE_BLUEPRINT_REGEX.search(blueprint_line)
        idx, robot_blueprints_text = match_b.groups()

        robot_blueprint_map = {}
        for match_r in re.finditer(LINE_ROBOT_REGEX, robot_blueprints_text):
            robot_blueprint = match_r.groups()
            costs = {}
            costs[robot_blueprint[2]] = int(robot_blueprint[1])
            if robot_blueprint[4]:
                costs[robot_blueprint[4]] = int(robot_blueprint[3])
            robot_blueprint_map[robot_blueprint[0]] = costs

        blueprints_map[int(idx)] = robot_blueprint_map

    return blueprints_map


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read i[]nput data from file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - Blueprint quality sum (24 mins) = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - Top 3 Blueprint quality sum (32 mins) = {answer02}')
