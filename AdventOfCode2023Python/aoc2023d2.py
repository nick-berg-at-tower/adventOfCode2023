import re

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# only 12 red cubes, 13 green cubes, and 14 blue cubes
# sum IDs of games that are possible
# sample should give 8

TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14


day = "2"
testing = False

class Game:

    def __init__(self, raw_game_input: str):
        self.raw_game = raw_game_input
        self.possible = True
        self.game = self.extractGameNumber()
        self.min_red = 0
        self.min_blue = 0
        self.min_green = 0
        self.extractGameNumber()
        self.extractGameStrings()
        self.power = self.min_red*self.min_green*self.min_blue

    def extractGameNumber(self):
        return int(self.raw_game.split(":")[0].split(" ")[1])

    def extractGameStrings(self):
        raw_draws = self.raw_game.split(":")[1].split(";")
        for draw in raw_draws:
            processed_draw = Draw(draw)
            self.possible = self.possible and processed_draw.valid
            self.min_red = max(self.min_red, processed_draw.red)
            self.min_green = max(self.min_green, processed_draw.green)
            self.min_blue = max(self.min_blue, processed_draw.blue)
        return raw_draws

class Draw:

    def __init__(self, draw_input):
        self.raw_draw = draw_input
        self.green = 0
        self.blue = 0
        self.red = 0
        for balls in draw_input.split(","):
            color = balls.strip().split(" ")
            if color[1] == 'red':
                self.red = int(color[0])
            elif color[1] == 'green':
                self.green = int(color[0])
            elif color[1] == 'blue':
                self.blue = int(color[0])
        self.valid = self.red <= TOTAL_RED and self.green <= TOTAL_GREEN and self.blue <= TOTAL_BLUE
        print(f'{self} {'is valid' if self.valid else 'is NOT valid'}')

    def __repr__(self):
        return f'Red:{self.red}, Green:{self.green}, Blue:{self.blue}'




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


def solvePart1():
    raw_input = LineParser().get_initial_state()
    sum = 0

    for line in raw_input:
        game = Game(line)
        game_number = game.extractGameNumber()
        game_strings = game.extractGameStrings()
        game_possible = game.possible
        print(f'Game {game_number} is {'possible' if game_possible else 'not possible'}')
        if game_possible:
            sum += game.extractGameNumber()
    print(f'Solution is {sum}')

def solvePart2():
    raw_input = LineParser().get_initial_state()
    sum = 0

    for line in raw_input:
        game = Game(line)
        game_number = game.extractGameNumber()
        game_possible = game.possible
        print(f'Game {game_number} is {'possible' if game_possible else 'not possible'}')
        sum += game.power
    print(f'Solution is {sum}')



if __name__ == '__main__':
    # solvePart1()
    solvePart2()
