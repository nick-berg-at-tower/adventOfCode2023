import re
from enum import Enum

import numpy as np

# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# Expected output 374

day = "11"
testing = False


class LineParser:

    def __init__(self):
        input_data = self.load_input()
        self.initial_state = input_data

    def get_initial_state(self):
        return self.initial_state

    def load_input(self):
        input_path = f'./aoc2023/d{day}{"test" if testing else ""}.txt'
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


class StarMap:
    def __init__(self, rawInput):
        self.input_height = len(rawInput)
        self.input_width = len(rawInput[0].strip())
        self.array = np.zeros((self.input_height, self.input_width))
        for y in range(0, self.input_height):
            for x in range(0, self.input_width):
                self.array[y][x] = 0 if rawInput[y][x] == '#' else 1
        # print(self.array)
        self.galaxy_coords = []
        self.scale = 1

    def expand(self):
        new_rows = []
        for row in range(0, self.input_height):
            if sum(self.array[row, :]) == self.input_width:
                new_rows.append(row)
        new_cols = []
        for col in range(0, self.input_height):
            if sum(self.array[:, col]) == self.input_height:
                new_cols.append(col)
        self.add_row(new_rows)
        self.add_column(new_cols)

    def set_coords(self):
        for y in range(0, self.array.shape[0]):
            for x in range(0, self.array.shape[1]):
                if self.array[y, x] == 0:
                    self.galaxy_coords.append((y, x))

    def count_galaxy_distances(self):
        for y in range(0, self.array.shape[0]):
            for x in range(0, self.array.shape[1]):
                if self.array[y, x] == 0:
                    self.array[y, x] = 1

    def add_column(self, index):
        self.array = np.insert(self.array, index, self.scale, axis=1)

    def add_row(self, index):
        self.array = np.insert(self.array, index, self.scale, axis=0)
        # print(self.array)


def solvePart1():
    pass


def solvePart2():
    pass


if __name__ == '__main__':
    rawInput = LineParser().get_initial_state()
    star_map = StarMap(rawInput)
    star_map.scale = 999999
    star_map.expand()
    star_map.set_coords()
    total_distance = 0
    print(star_map.galaxy_coords)
    star_map.count_galaxy_distances()
    while len(star_map.galaxy_coords) > 0:
        galaxy = star_map.galaxy_coords.pop()
        for remaining_galaxy in star_map.galaxy_coords:
            total_distance += sum(
                star_map.array[min(galaxy[0], remaining_galaxy[0]):max(galaxy[0], remaining_galaxy[0]),
                galaxy[1]]) + sum(
                star_map.array[galaxy[0], min(remaining_galaxy[1], galaxy[1]):max(remaining_galaxy[1], galaxy[1])])
            # print(
            #     f'{star_map.array[min(galaxy[0], remaining_galaxy[0]):max(galaxy[0], remaining_galaxy[0]), galaxy[1]]} sum = {sum(star_map.array[min(galaxy[0], remaining_galaxy[0]):max(galaxy[0], remaining_galaxy[0]), galaxy[1]])}')
            # print(
            #     f'{star_map.array[galaxy[0], min(remaining_galaxy[1], galaxy[1]):max(remaining_galaxy[1], galaxy[1])]} sum = {sum(star_map.array[galaxy[0], min(remaining_galaxy[1], galaxy[1]):max(remaining_galaxy[1], galaxy[1])])}')
    print(total_distance)
