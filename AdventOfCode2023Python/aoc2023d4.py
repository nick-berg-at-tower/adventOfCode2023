import math
import re

import numpy as np

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
# Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Card 5 has no winning numbers, so it is worth no points.
# Card 6 has no winning numbers, so it is worth no points.

day = "4"
testing = False

class Game:

    def __init__(self, raw_game_input: str):
        raw_game_number, raw_game = raw_game_input.strip().split(":")
        self.game_number = int(re.split("[ ]+",raw_game_number)[1])
        raw_winning_numbers, raw_player_numbers = raw_game.strip().split("|")
        self.winning_numbers = [int(number) for number in re.split("[ ]+",raw_winning_numbers.strip())]
        self.player_numbers = [int(number) for number in re.split("[ ]+",raw_player_numbers.strip())]
        self.matching_numbers = 0
        self.score = 0
        for number in self.winning_numbers:
            if number in self.player_numbers:
                self.matching_numbers += 1
        if self.matching_numbers>0:
            self.score = pow(2, self.matching_numbers-1)

    def __repr__(self):
        return (f'Game: {self.game_number}\n'
                f'Winning Numbers: {self.winning_numbers}\n'
                f'Player Numbers: {self.player_numbers}\n'
                f'Score = {self.score}')



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
        sum += Game(line).score
    print(f'Solution is {sum}')

def solvePart2():
    raw_input = LineParser().get_initial_state()
    card_counts = np.ones(len(raw_input))
    for index in range(0,len(raw_input)):
        score = Game(raw_input[index]).matching_numbers
        print(f'Score = {score}')
        for game in range(1+index, min(len(card_counts), score+1+index)):
            card_counts[game] = card_counts[game]+card_counts[index]
    print(f'Solution is {card_counts.sum()}')
    print(card_counts)



if __name__ == '__main__':
    # solvePart1()
    solvePart2()
