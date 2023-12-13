import itertools
import re
import math

# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangement

day = "12"
testing = False

def unique_permutations(elements):
    if len(elements) == 1:
        yield (elements[0],)
    else:
        unique_elements = set(elements)
        for first_element in unique_elements:
            remaining_elements = list(elements)
            remaining_elements.remove(first_element)
            for sub_permutation in unique_permutations(remaining_elements):
                yield (first_element,) + sub_permutation

class Spring:
    def __init__(self, raw_spring_input: str, additional_coppies=0):
        self.raw_spring, self.raw_numbers = raw_spring_input.strip().split(" ")
        original_spring, original_numbers = raw_spring_input.strip().split(" ")
        for copy_number in range(0,additional_coppies):
            self.raw_spring = self.raw_spring + "?" + original_spring
            self.raw_numbers = self.raw_numbers+","+original_numbers
        self.numerical_summary = [int(number) for number in self.raw_numbers.split(",")]
        self.question_marks = self.raw_spring.count('?')
        self.known_broken_springs = self.raw_spring.count('#')
        self.total_broken_springs = sum(self.numerical_summary)
        self.broken_springs_to_be_assigned = self.total_broken_springs - self.known_broken_springs
        simplest_order = list(itertools.repeat('#',self.broken_springs_to_be_assigned))+list(itertools.repeat('.',self.question_marks-self.broken_springs_to_be_assigned))
        # self.all_orders = set(unique_permutations(simplest_order))
        # self.valid_orders = self.get_valid_orders()


        # print(self.raw_spring)
        # print(self.raw_numbers)
    def calcualte_numerical_summary(self, test_spring):
        return [len(broken) for broken in test_spring.split(".") if broken!='']

    def get_valid_orders(self):
        valid_orders = []
        for order in self.all_orders:
            test_spring = ""
            order_index = 0
            for index in range(0,len(self.raw_spring)):
                if self.raw_spring[index]=='?':
                    test_spring = test_spring+order[order_index]
                    order_index += 1
                else:
                    test_spring = test_spring+self.raw_spring[index]
            if self.calcualte_numerical_summary(test_spring)==self.numerical_summary:
                valid_orders.append(order)
        return valid_orders

    def __repr__(self):
        return (f'Raw input: {self.raw_spring+" "+self.raw_numbers} \n'
                f'Spring {self.raw_spring} with numerical data {self.numerical_summary} \n'
                f'Known Broken Springs = {self.known_broken_springs} and Total Broken Springs = {self.total_broken_springs}\n'
                f'Assingable broken springs = {self.broken_springs_to_be_assigned}\n'
                f'Possibilities {math.factorial(self.question_marks)/(math.factorial(self.question_marks-self.broken_springs_to_be_assigned)*math.factorial(self.broken_springs_to_be_assigned))}'
                f'\n')



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
    question_marks = []
    solution = 0
    line_index = 0
    for line in raw_input:
        print(f'Processing line {line_index}')
        line_index += 1
        spring = Spring(line)
        question_marks.append(spring.raw_spring.count('?'))
        print(spring)
        print(len(spring.valid_orders))
        solution += len(spring.valid_orders)
    print(f'Solution is {solution}')

def solvePart2():
    raw_input = LineParser().get_initial_state()
    question_marks = []
    solution = 0
    line_index = 0
    for line in raw_input:
        print(f'Processing line {line_index}')
        line_index += 1
        spring = Spring(line,4)
        question_marks.append(spring.raw_spring.count('?'))
        print(spring)
        # print(len(spring.valid_orders))
        # solution += len(spring.valid_orders)
    print(f'Solution is {solution}')



if __name__ == '__main__':
    # solvePart1()
    solvePart2()
