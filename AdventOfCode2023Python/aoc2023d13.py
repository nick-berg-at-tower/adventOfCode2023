import re
from enum import Enum

import numpy as np
#
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#
# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
#
# Expect column 5, then row, 4 for solution 405


day = "13"
testing = False


class LineParser:

    def __init__(self):
        input_data = self.load_input()
        clean_data = []
        current_sample = []
        for line in input_data:
            if line.strip()=="":
                clean_data.append(current_sample)
                current_sample = []
            else:
                current_sample.append(line.strip())
        clean_data.append(current_sample)
        self.initial_state = clean_data

    def get_initial_state(self):
        return self.initial_state

    def load_input(self):
        input_path = f'./aoc2023/d{day}{"test" if testing else ""}.txt'
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


class AshMap:
    def __init__(self, rawMap):
        self.input_height = len(rawMap)
        self.input_width = len(rawMap[0])
        self.array = np.zeros((self.input_height, self.input_width), dtype=bool)
        for y in range(0, self.input_height):
            for x in range(0, self.input_width):
                self.array[y][x] = False if rawMap[y][x] == '.' else True
        self.possible_col_reflections = range(1, self.input_width)
        self.possible_row_reflections = range(1,self.input_height)
        self.reflection_col = 0
        self.reflection_row = 0

    def find_reflection(self):
        for possible_col in self.possible_col_reflections:
            if self.test_reflection(possible_col):
                print(f'Found an col rotation at axis = {possible_col}')
                return True
        for possible_row in self.possible_row_reflections:
            if self.test_reflection(possible_row, isCol=False):
                print(f'Found an row rotation at axis = {possible_row}')
                return True
        return False


    def test_reflection(self, axis, isCol=True):
        test_array = self.array if isCol else self.array.transpose()
        reflection_radius = min(axis, (self.input_width if isCol else self.input_height)-axis)
        # sub_array = self.array()
        left_array = test_array[:,axis-reflection_radius:axis]
        right_array = test_array[:,axis+reflection_radius-1:axis-1:-1]
        for row, row_reflection in zip(left_array, right_array):
            # print(f'{row} = {row_reflection} is {all(row==row_reflection)}')
            if not all(row==row_reflection):
                return False
        if isCol:
            self.reflection_col = axis
        else:
            self.reflection_row = axis
        return True

class SmudgeAshMap:
    def __init__(self, rawMap):
        self.input_height = len(rawMap)
        self.input_width = len(rawMap[0])
        self.array = np.zeros((self.input_height, self.input_width), dtype=bool)
        for y in range(0, self.input_height):
            for x in range(0, self.input_width):
                self.array[y][x] = False if rawMap[y][x] == '.' else True
        self.possible_col_reflections = range(1, self.input_width)
        self.possible_row_reflections = range(1,self.input_height)
        self.reflection_col = 0
        self.reflection_row = 0

    def find_reflection(self):
        for possible_col in self.possible_col_reflections:
            if self.test_reflection(possible_col):
                print(f'Found an col rotation at axis = {possible_col}')
                return True
        for possible_row in self.possible_row_reflections:
            if self.test_reflection(possible_row, isCol=False):
                print(f'Found an row rotation at axis = {possible_row}')
                return True
        return False


    def test_reflection(self, axis, isCol=True):
        test_array = self.array if isCol else self.array.transpose()
        reflection_radius = min(axis, (self.input_width if isCol else self.input_height)-axis)
        # sub_array = self.array()
        left_array = test_array[:,axis-reflection_radius:axis]
        right_array = test_array[:,axis+reflection_radius-1:axis-1:-1]
        imperfections = 0
        for row, row_reflection in zip(left_array, right_array):
            print(f'{row} = {row_reflection} is {sum(row!=row_reflection)}')
            imperfections += sum(row!=row_reflection)
            if imperfections > 1:
                return False
        if imperfections==1:
            if isCol:
                self.reflection_col = axis
            else:
                self.reflection_row = axis
            return True
        return False


def solvePart1():
    cleanInput = LineParser().get_initial_state()
    sum = 0
    print("first map")
    for map in cleanInput:
        ashMap = AshMap(map)
        ashMap.find_reflection()
        print("")
        print("next map:")
        sum += ashMap.reflection_col + ashMap.reflection_row*100
    print(f'Solution is {sum}')



def solvePart2():
    cleanInput = LineParser().get_initial_state()
    sum = 0
    print("first map")
    for map in cleanInput:
        ashMap = SmudgeAshMap(map)
        ashMap.find_reflection()
        print("")
        print("next map:")
        sum += ashMap.reflection_col + ashMap.reflection_row * 100
    print(f'Solution is {sum}')


if __name__ == '__main__':
    solvePart2()