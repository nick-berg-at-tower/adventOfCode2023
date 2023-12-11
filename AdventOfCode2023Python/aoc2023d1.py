import re

day = "1"
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


def solvePart1():
    raw_input = LineParser().get_initial_state()
    pattern = re.compile('\\d')
    sum = 0
    for line in raw_input:
        numbers = pattern.findall(line)
        sum += int(numbers[0]) * 10 + int(numbers[len(numbers) - 1])
    print(f'Solution is {sum}')


def replaceWithDigit(text: str):
    digits = (
        ("twoneight", 218),
        ("eightwone", 821),
        ("eighthree", 83),
        ("eightwone", 821),
        ("threeightwo", 382),
        ("threeightwhree", 383),
        ("oneight", 18),
        ("fiveight", 58),
        ("threeight", 38),
        ("twone", 21),
        ("eightwo", 82),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9)
    )
    newtext=text
    offset = 0
    for digit in digits:
        if text.find(digit[0])>=0:
            print(f'found {digit[1]} in {text}')
            newtext = newtext.replace(digit[0],str(digit[1]))
            # print(newtext)
        # location = text.find(digit[0])
        # if location >= 0:
        #     newtext = newtext[:location+offset] + str(digit[1]) + newtext[location+offset:]
        #     offset += 1
    return newtext


def solvePart2():
    raw_input = LineParser().get_initial_state()
    pattern = re.compile('\\d')
    sum = 0
    for line in raw_input:
        # print(line)
        # print(replaceWithDigit(line))
        newline = replaceWithDigit(line)
        numbers = pattern.findall(newline)
        # print(int(numbers[0]) * 10 + int(numbers[len(numbers) - 1]))
        extract = int(numbers[0]) * 10 + int(numbers[len(numbers) - 1])
        sum += extract
        # print(f'Extracted {newline.strip()} from {line.strip()} giving {extract}')
    print(f'Solution is {sum}')


if __name__ == '__main__':
    solvePart2()
    # testString = "123456789"
    # print(testString[:12])
    # print(testString[12:])
