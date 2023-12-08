#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 07: No Space Left On Device
"""
import os
import re

COMMAND_CD = re.compile(r'\$ cd (.*)')
COMMAND_LS = re.compile(r'\$ ls')
LISTING_DIR = re.compile(r'dir (.*)')
LISTING_FILE = re.compile(r'(\d+) (.*)')


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child_folder = {}
        self.child_file = {}

    def __repr__(self):
        return os.path.join(str(self.parent), self.name)

    def add_child_folder(self, name):
        if name not in self.child_folder.keys():
            child = Folder(name, self)
            self.child_folder[name] = child
        else:
            child = self.child_folder[name]
        return child

    def add_child_file(self, name, size):
        if name not in self.child_file.keys():
            self.child_file[name] = int(size)
        else:
            exit('duplicate filename?')
        return name

    def size(self):
        size = 0
        for n, f in self.child_folder.items():
            s = f.size()
            size += s
            # print(self.name, f, size, s)
        for name, s in self.child_file.items():
            size += s
            # print(self.name, name, size, s)
        return size


def part01(input_data):
    answer = solve(input_data)
    return answer[0]


def part02(input_data):
    answer = solve(input_data)
    return answer[1]


def solve(terminal_output):
    # process terminal output
    folder_list = []
    folder_root = Folder('#ROOT#', None)
    folder_current = folder_root

    for line in terminal_output:
        if match := COMMAND_CD.search(line):
            name = match.group(1)
            if name == '..':
                folder_current = folder_current.parent
            else:
                folder_current = folder_current.add_child_folder(name)
                folder_list.append(folder_current)
        elif COMMAND_LS.search(line):
            # print('do nothing - ', line, folder_current)
            continue
        else:
            if match := LISTING_FILE.search(line):
                name = match.group(2)
                size = match.group(1)
                folder_current.add_child_file(name, size)
            elif match := LISTING_DIR.search(line):
                # print('do nothing - ', line, match.group(1), folder_current)
                continue

    # part 01
    part01_folder_sum = sum([f.size() for f in folder_list if f.size() <= 100000])

    # part 02
    file_system_size = 70000000
    space_update = 30000000
    folder_root_size = folder_root.size()

    space_unused = file_system_size - folder_root_size
    space_required = space_update - space_unused

    folder_list_space = [(f, f.size()) for f in folder_list if f.size() >= space_required]
    folder_list_sorted = sorted(folder_list_space, key=lambda x: x[1])
    shortest_folder = folder_list_sorted.pop(0)
    part02_folder_size = shortest_folder[1]

    return (part01_folder_sum, part02_folder_size)


def parse_data(input_data):
    return input_data.splitlines()


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer = solve(input_data)
    print(f'part01 - Total sizes of those directories less than 100000 is {answer[0]}')

    # answer = solve(input_data)
    print(f'part02 - Size of smallest directory to free space = {answer[1]}')
