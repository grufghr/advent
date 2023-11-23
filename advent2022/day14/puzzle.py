#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 14: Regolith Reservoir
"""
import os
import numpy as np
import matplotlib
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

COLOR_MAP = matplotlib.colors.LinearSegmentedColormap.from_list(
    "height_gradient_map", ["white", "black", "blue"], 256
)

AIR = int(0)
ROCK = 1
SAND = 2
SAND_ENTRY = (0, 500)


class SandSimulator:
    def __init__(self, rock_drawing, infinite_floor=False):
        coord_list = self._parse_rock_drawing(rock_drawing)

        # create self.grid
        self._create_grid(coord_list, infinite_floor)

        self.sand_count = 0
        self.sand_fall_start()

    def _parse_rock_drawing(self, rock_drawing):
        # extract all points text '(nnn,nn)' into list
        coord_text = [[t.strip() for t in line.split("->")] for line in rock_drawing]
        # convert text into tuple
        coord_list = [[tuple(map(int, t.split(","))) for t in x] for x in coord_text]
        # swap into (row, col) format
        coord_list = [[(c[1], c[0]) for c in x] for x in coord_list]

        return coord_list

    def _create_grid(self, coord_list, infinite_floor):
        # determine boundaries
        coord_row = [r[0] for sub in coord_list for r in sub]
        coord_col = [r[1] for sub in coord_list for r in sub]
        bounds_n = 0
        bounds_w = min(coord_col) if not infinite_floor else 0
        bounds_s = max(coord_row)
        m = SAND_ENTRY[1] * 2
        bounds_e = max(coord_col) if not infinite_floor else m
        # apply boundaries to coordinates
        border_n = 0
        border_e = 2
        border_s = 3
        border_w = 1
        size_c = bounds_e - bounds_w + border_e + border_w
        size_r = bounds_s - bounds_n + border_n + border_s
        coord_list = [
            [(c[0] - bounds_n + border_n, c[1] - bounds_w + border_w) for c in x]
            for x in coord_list
        ]

        # create a numpy array canvas
        self.grid = np.array([[AIR] * size_c for i in range(size_r)])

        # location of sand entry & first sand drop (0, 500)
        self.loc_sand_entry = (border_n, SAND_ENTRY[1] - bounds_w + border_w)

        # draw rock formations
        for rockform in coord_list:
            loc_s = rockform[0]
            for loc_e in rockform[1:]:
                # print(loc_s, loc_e)
                sr = min(loc_s[0], loc_e[0])
                er = max(loc_s[0], loc_e[0])
                sc = min(loc_s[1], loc_e[1])
                ec = max(loc_s[1], loc_e[1])
                if (sr == er) or (sc == ec):
                    er += 1
                    ec += 1
                self.grid[sr:er, sc:ec] = ROCK
                loc_s = loc_e

        if infinite_floor:
            self.grid[size_r - 1, :] = ROCK

        return self.grid

    def sand_fall_start(self):
        self.loc_sand = self.loc_sand_entry

        if self.grid[self.loc_sand] == SAND:
            # print(f"Sand grain {self.sand_count} has blocked sand entry")
            self.sand_falling = False
            return

        self.grid[self.loc_sand] = SAND
        self.sand_count += 1
        self.sand_falling = True

    def sand_fall_next(self):
        if not self.sand_falling:
            return

        if self.loc_sand[0] + 1 >= self.grid.shape[0]:
            # print(f"Sand grain {self.sand_count} falling into the abyss")
            self.sand_falling = False  # stop further sand falling
            self.sand_count -= 1  # remove last count as it fell into abyss
            return

        loc_n = (self.loc_sand[0] + 1, self.loc_sand[1])
        if self.grid[loc_n] == AIR:
            self.grain_fall(loc_n)
        else:
            loc_n = (self.loc_sand[0] + 1, self.loc_sand[1] - 1)
            if self.grid[loc_n] == AIR:
                self.grain_fall(loc_n)
            else:
                loc_n = (self.loc_sand[0] + 1, self.loc_sand[1] + 1)
                if self.grid[loc_n] == AIR:
                    self.grain_fall(loc_n)
                else:
                    self.sand_fall_start()

    def grain_fall(self, loc_n):
        self.grid[loc_n] = SAND
        self.grid[self.loc_sand] = AIR
        self.loc_sand = loc_n


class SandVisualiser:
    def __init__(self, simulator):
        self.sim = simulator

    def show(self):
        fig, gsub = pyplot.subplots(1, 1)
        self.g1 = gsub.imshow(self.sim.grid, interpolation="nearest", cmap=COLOR_MAP)
        gsub.set_title("Sand Simulation")
        gsub.set_aspect("equal")
        gsub.axis("off")
        self.animation = FuncAnimation(fig, self.update, frames=20, interval=0)
        self.animation.pause()
        self.paused = True
        fig.canvas.mpl_connect("button_press_event", self.toggle_pause)
        pyplot.colorbar(self.g1, cmap=COLOR_MAP, orientation="horizontal")
        pyplot.show()
        print("Starting paused - click on animation simulation window")

    def toggle_pause(self, *args, **kwargs):
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, framenumber):
        if not self.sim.sand_falling:
            self.paused = True
            self.animation.pause()
            return

        self.sim.sand_fall_next()

        self.g1.set_data(self.sim.grid)

        pyplot.draw()


def solve01(input_data):
    answer = solve(input_data, False, False)
    return answer


def solve02(input_data):
    answer = solve(input_data, True, False)
    return answer


def solve(input_text_rock_drawing, infinite_floor, visualise=False):
    simulator = SandSimulator(input_text_rock_drawing, infinite_floor)

    if not visualise:
        while simulator.sand_falling:
            simulator.sand_fall_next()
    else:
        visual = SandVisualiser(simulator)
        visual.show()

    units_of_sand = simulator.sand_count

    return units_of_sand


def parse_data(input_data):
    return input_data.splitlines()


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, "r") as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - Sand count thats falls into abyss = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - Sand count when entry point block = {answer02}")
