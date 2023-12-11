import re
from enum import Enum

import numpy as np

# Expected Output is 4361

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
#

day = "7"
testing = False

CardValue = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}

HandStrength = {
    'FiveOfAKind': 10,
    'FourOfAKind': 9,
    'FullHouse': 8,
    'ThreeOfAKind': 7,
    'TwoPair': 6,
    'OnePair': 5,
    'HighCard': 4
}


class Hand:
    def __init__(self, rawHandandValue):
        self.rawHand, self.rawValue = rawHandandValue.strip().split(" ")
        self.hand_strength = 'HighCard'
        self.hand_rank = 0
        self.hand_bid = int(self.rawValue)
        self.card_count = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            'T': 0,
            'J': 0,
            'Q': 0,
            'K': 0,
            'A': 0
        }
        for card in self.rawHand:
            self.card_count[f'{card}'] += 1
        self.applyJokerRule()
        self.evaluateHandStrength()
        print(f'{self.rawHand} with joker rule became {self.hand_strength}')

    def applyJokerRule(self):
        mostCommonCard = [key for m in [max(self.card_count.values())] for key,val in self.card_count.items() if val == m][0]
        if mostCommonCard!= 'J':
            self.card_count[mostCommonCard] += self.card_count['J']
            self.card_count['J'] = 0
        else:
            j_count = self.card_count['J']
            self.card_count['J'] = 0
            mostCommonCard = \
            [key for m in [max(self.card_count.values())] for key, val in self.card_count.items() if val == m][0]
            self.card_count[mostCommonCard] += j_count


    def evaluateHandStrength(self):
        countList = list(self.card_count.values())
        if (5 in countList):
            self.hand_strength = 'FiveOfAKind'
        elif (4 in countList):
            self.hand_strength = 'FourOfAKind'
        elif (3 in countList):
            if (2 in countList):
                self.hand_strength = 'FullHouse'
            else:
                self.hand_strength = 'ThreeOfAKind'
        elif countList.count(2) == 2:
            self.hand_strength = 'TwoPair'
        elif (max(self.card_count.values()) == 2):
            self.hand_strength = 'OnePair'

    def __repr__(self):
        return f'{self.card_count}, {str(self.hand_bid)}, {self.hand_strength}, {self.rawHand}'

    def __lt__(self, other):
        if (self.hand_strength == other.hand_strength):
            for cardIndex in range(0,5):
                if self.rawHand[cardIndex]!=other.rawHand[cardIndex]:
                    lessThan =  CardValue.get(self.rawHand[cardIndex]) < CardValue.get(other.rawHand[cardIndex])
                    # print(f'Determined {lessThan} when evaluating {self} < {other} using CardValue')
                    return lessThan
            # print(f'Determined False when evaluating {self} < {other}')
            return False
        else:
            lessThan =  (HandStrength.get(self.hand_strength) < HandStrength.get(other.hand_strength))
            # print(f'Determined {lessThan} when evaluating {self} < {other} using HandStrength')
            return lessThan

    def __gt__(self, other):
        if self.hand_strength == other.hand_strength:
            for cardIndex in range(0,5):
                if self.rawHand[cardIndex]!=other.rawHand[cardIndex]:
                    return CardValue.get(self.rawHand[cardIndex]) > CardValue.get(other.rawHand[cardIndex])
            return False
        else:
            return HandStrength.get(self.hand_strength) > HandStrength.get(self.hand_strength)

    def __eq__(self, other):
        return self.rawHand==other.rawHand

    def __le__(self, other):
        return (self.__lt__(other) or self.__eq__(other))

    def __ge__(self, other):
        return (self.__gt__(other) or self.__eq__(other))


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
    pass


def solvePart2():
    pass


if __name__ == '__main__':
    rawInput = LineParser().get_initial_state()
    all_hands = []
    for line in rawInput:
        this_hand = Hand(line)
        all_hands.append(this_hand)
    for hand in all_hands:
        print(hand)
    print("Sorting")
    all_hands.sort()
    handCount = 1
    for hand in all_hands:
        hand.hand_rank = handCount
        print(hand)
        handCount += 1
    print(sum(hand.hand_bid*hand.hand_rank for hand in all_hands))
