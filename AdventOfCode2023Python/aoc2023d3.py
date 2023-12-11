import re

import numpy as np

# Expected Output is 4361

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

day = "3"
testing = True


class Digit:

    def __init__(self, value, y, x):
        self.value = value
        self.y = y
        self.x = x

    def __repr__(self):
        return f'{self.value} at y={self.y}, x={self.x}'


class Number:
    def __init__(self):
        self.digits = []
        self.value = 0
        self.surrounding = ""
        self.is_part = False

    def add_digit(self, new_digit):
        self.digits.append(new_digit)
        self.value = self.value * 10 + int(new_digit.value)

    def getSurrondings(self, grid):
        start = {'x': self.digits[0].x - 1, 'y': self.digits[0].y - 1}
        end = {'x': self.digits[-1].x + 1, 'y': self.digits[-1].y + 1}
        surroundings = ""
        for row in range(max(start.get('y'), 0), min(end.get('y')+1, len(grid))):
            for col in range(max(start.get('x'), 0), min(end.get('x')+1, len(grid[0]))):
                if (not grid[row][col].isdigit()):
                    surroundings += grid[row][col]
        self.surrounding = surroundings
        self.is_part = len(self.surrounding.replace('.',''))>0
        return surroundings

    def __repr__(self):
        if len(self.digits) > 0:
            return f'{self.value} from x={self.digits[0].x}, y={self.digits[0].y}, to x={self.digits[-1].x}, y={self.digits[-1].y}'
        else:
            return "NaN"


class Gear:
    def __init__(self, grid, y, x):
        self.location = (y, x)
        self.surrounding = self.getSurrondings(grid)
        self.number_one = 1
        self.number_two = 2
        self.ratio = 1

    def getRatio(self):
        return self.ratio

    def getSurrondings(self, grid):
        start = (self.location[1] - 1, self.location[0] - 1)
        end = (self.location[1] + 1, self.location[0] + 1)
        surroundings = ""
        for row in range(max(start[1], 0), min(end[1]+1, len(grid))):
            for col in range(max(start[0], 0), min(end[0]+1, len(grid[0]))):
                if (grid[row][col].isdigit()):
                    number = int(grid[row][col])
                    digits = []
                    print(f'I found a digit {grid[row][col]} at {col},{row}')
                    # need to fix this digits.append(grid[row][col])
                    print(f'Lets see how many digits this number has?')
                    print(f'First lets go left')
                    search_row = row
                    search_col = col-1
                    while grid[search_row][search_col].isdigit():
                        print(f'I found another digit {grid[search_row][search_col]} at {search_col},{search_row}')
                        number = number+pow(10,col-search_col)*int(grid[search_row][search_col])
                        print(f'the number is now {number}')
                        search_col += -1
                    print(f'now lets go right')
                    search_row = row
                    search_col = col + 1
                    while grid[search_row][search_col].isdigit():
                        print(f'I found another digit {grid[search_row][search_col]} at {search_col},{search_row}')
                        number = number*10+int(grid[search_row][search_col])
                        print(f'the number is now {number}')
                        search_col += 1
                    print(f'The final number is {number}')
                    Digit(grid[row][col],row,col)
                surroundings += grid[row][col]
        self.surrounding = surroundings
        return surroundings



class LineParser:

    def __init__(self):
        input_data = self.load_input()
        height = len(input_data)
        width = len(input_data[0])
        grid = []
        for y in range(0, height):
            line = []
            for x in range(0, width - 1):
                line.append(input_data[y][x])
            grid.append(line)
        self.initial_state = np.array(grid)

    def get_initial_state(self):
        return self.initial_state

    def load_input(self):
        input_path = f'./aoc2023/d{day}{"test" if testing else ""}.txt'
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


def solvePart1():
    sum = 0
    state = LineParser().get_initial_state()
    number = Number()
    for y in range(state.shape[0]):
        if number.value > 0:
            # print(f'Found Number {number}')
            number.getSurrondings(state)
            if number.is_part:
                sum += number.value
        number = Number()
        for x in range(state.shape[1]):
            if state[y][x].isdigit():
                digit = Digit(state[y][x], y, x)
                # print(digit)
                number.add_digit(digit)
            else:
                if number.value > 0:
                    # print(f'Found Number {number}')
                    number.getSurrondings(state)
                    if number.is_part:
                        sum += number.value
                number = Number()
    print(f'Solution is {sum}')


def solvePart2():
    sum = 0
    state = LineParser().get_initial_state()
    height, width = state.shape
    gears = []
    for y in range(0,height):
        for x in range(0,width):
            if state[y][x]=='*':
                gear = Gear(state,y,x)
                gears.append(gear)
    sumOfRatios = 0
    for gear in gears: sumOfRatios += gear.ratio
    for gear in gears: print(gear.surrounding)
    print(sumOfRatios)


if __name__ == '__main__':
    solvePart2()
