import re
from enum import Enum

import numpy as np

# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
#
# OOOO.#.O.. 10
# OO..#....#  9
# OO..O##..O  8
# O..#.OO...  7
# ........#.  6
# ..#....#.#  5
# ..O..#.O.O  4
# ..O.......  3
# #....###..  2
# #....#....  1
#
# Expect after NORTH 136


day = "14"
testing = True


class LineParser:

    def __init__(self):
        input_data = self.load_input()
        clean_data = []
        for line in input_data:
            clean_data.append(line.strip())
        self.initial_state = clean_data

    def get_initial_state(self):
        return self.initial_state

    def load_input(self):
        input_path = f'./aoc2023/d{day}{"test" if testing else ""}.txt'
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


class RockMap:
    def __init__(self, rawMap):
        self.input_height = len(rawMap)
        self.input_width = len(rawMap[0])
        self.array = np.zeros((self.input_height, self.input_width), dtype=str)
        for y in range(0, self.input_height):
            for x in range(0, self.input_width):
                self.array[y][x] = rawMap[y][x]

    def tilt_up(self):
        for y in range(1, self.input_height):
            for x in range(0, self.input_width):
                self.roll_up(y, x)

    def tilt_left(self):
        for x in range(1, self.input_width):
            for y in range(0, self.input_height):
                self.roll_left(y, x)

    def tilt_down(self):
        for y in range(self.input_height-1,-1, -1):
            for x in range(0, self.input_width):
                self.roll_down(y, x)

    def tilt_right(self):
        for x in range(self.input_width-1, -1, -1):
            for y in range(0, self.input_height):
                self.roll_right(y, x)

    def roll_up(self, y, x):
        if y>0 and self.array[y][x] == 'O' and self.array[y - 1][x] == '.':
            self.array[y][x] = '.'
            self.array[y - 1][x] = 'O'
            self.roll_up(y - 1, x)

    def roll_down(self, y, x):
        if y<self.input_height-1 and self.array[y][x] == 'O' and self.array[y + 1][x] == '.':
            self.array[y][x] = '.'
            self.array[y + 1][x] = 'O'
            self.roll_down(y + 1, x)

    def roll_left(self, y, x):
        if x>0 and self.array[y][x] == 'O' and self.array[y][x-1] == '.':
            self.array[y][x] = '.'
            self.array[y][x-1] = 'O'
            self.roll_left(y , x-1)

    def roll_right(self, y, x):
        if x<(self.input_width-1) and self.array[y][x] == 'O' and self.array[y][x+1] == '.':
            self.array[y][x] = '.'
            self.array[y][x + 1] = 'O'
            self.roll_right(y, x + 1)

    def find_reflection(self):
        return False

    def test_reflection(self, axis, isCol=True):
        return False


def solvePart1():
    cleanInput = LineParser().get_initial_state()
    rock_map = RockMap(cleanInput)
    rock_map.tilt_up()
    score = len(cleanInput)
    solution = 0
    for line in rock_map.array:
        print(line)
        rock_score = score*sum([(1 if square == 'O' else 0) for square in line])
        print(f'Rock Score = {rock_score}')
        solution += rock_score
        score += -1
    print(f'Solution is {solution}')


def solvePart2():
    cleanInput = LineParser().get_initial_state()
    rock_map = RockMap(cleanInput)
    for cycle in range(0,1000000000):
        if cycle % 100000==0:
            print(f'Proccessed {cycle} cycles')
        rock_map.tilt_up()
        rock_map.tilt_left()
        rock_map.tilt_down()
        rock_map.tilt_right()
    score = len(cleanInput)
    solution = 0
    for line in rock_map.array:
        # print(line)
        rock_score = score * sum([(1 if square == 'O' else 0) for square in line])
        # print(f'Rock Score = {rock_score}')
        solution += rock_score
        score += -1
    print(f'Solution is {solution}')


if __name__ == '__main__':
    solvePart2()
