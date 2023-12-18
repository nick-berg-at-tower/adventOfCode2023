# imports go here
import timeit

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# only 12 red cubes, 13 green cubes, and 14 blue cubes
# sum IDs of games that are possible
# sample should give 8

# Globals Go here

day = "5"
testing = False


class LineParser:

    def __init__(self):
        input_data = self.load_input()
        self.initial_state = input_data
        data = []
        data_block = []
        for line in input_data:
            if line.strip() == '':
                data.append(data_block)
                data_block = []
            else:
                data_block.append(line.strip())
        data.append(data_block)
        self.seeds = data[0]
        self.maps = data[1:]

    def get_initial_state(self):
        return self.initial_state

    def load_input(self):
        input_path = f'./aoc2023/d{day}{"test" if testing else ""}.txt'
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


class SeedMapping:
    def __init__(self, input_strings):
        self.name = input_strings[0].split(" ")[0]
        self.mappings = []
        self.reverse_mappings = []
        for map_value in input_strings[1:]:
            map_values = [int(map_value) for map_value in map_value.split(" ")]
            start = map_values[1]
            stop = map_values[1] + map_values[2]
            adjustment = map_values[0] - map_values[1]
            self.mappings.append((start, stop, adjustment))
        for mapping in self.mappings:
            self.reverse_mappings.append((mapping[0] + mapping[2], mapping[1] + mapping[2], -mapping[2]))
        self.reverse_mappings.reverse()

    def map(self, input):
        for submapping in self.mappings:
            if submapping[0] <= input < submapping[1]:
                return input + submapping[2]
        return input

    def map_reverse(self, input):
        for submapping in self.reverse_mappings:
            if submapping[0] <= input < submapping[1]:
                return input + submapping[2]
        return input


def solvePart1():
    lineParser = LineParser()
    seeds = [int(seed) for seed in lineParser.seeds[0].split(" ")[1:]]
    # print(f'Seeds = {lineParser.seeds}')
    # print("Maps = ")
    maps = [SeedMapping(seed_map) for seed_map in lineParser.maps]
    # print(maps)
    # print(maps[0].map(100))
    # print(seeds)
    # print(lineParser.maps[0])
    test_map = ['seed-to-soil map:', '50 98 2', '52 50 48']
    seed_to_soil = SeedMapping(test_map)
    # print(seed_to_soil.map(51))

    min_value = 1000000000000000000000000000
    min_seed = 0

    for seed in seeds:
        original_seed = seed
        # print(f'Mapping seed {seed}')
        for map in maps:
            new_value = map.map(seed)
            # print(f'Mapping {seed} -> {new_value} using {map.name}')
            seed = new_value
        # print(f'Location is {seed}')
        if seed < min_value:
            min_seed = original_seed
            min_value = seed
    print(f'Expecting seed {13 if testing else 111959634} at location {35 if testing else 322500873}')
    print(f'The minimum seed is {min_seed} at {min_value}')


#     The minimum seed is 111959634 at 322500873

def find_overlap(seed_ranges):
    print('original seed ranges')
    print(seed_ranges)
    for x in range(0, len(seed_ranges)):
        for y in range(0, len(seed_ranges)):
            if x != y and seed_ranges[x][1] >= seed_ranges[y][0] and seed_ranges[x][0] <= seed_ranges[y][1]:
                print(f'Overlap between {seed_ranges[x]} and {seed_ranges[y]}')


def solvePart2():
    lineParser = LineParser()
    seeds = [int(seed) for seed in lineParser.seeds[0].split(" ")[1:]]
    maps = [SeedMapping(seed_map) for seed_map in lineParser.maps]

    seed_ranges = []
    for x in range(0, len(seeds), 2):
        seed_ranges.append((seeds[x], seeds[x] + seeds[x + 1]))

    maps.reverse()
    totaltimestart = timeit.default_timer()
    total_checks = 4145746192
    # total_checks = 1
    for location in range(0, total_checks):
        if location % 1000000 == 0:
            totaltimeend = timeit.default_timer()
            print(
                f'Checked {location} locations in {totaltimeend - totaltimestart} or average of {(totaltimeend - totaltimestart) / total_checks} per check')
        seed_value = location
        for map in maps:
            seed_value = map.map_reverse(seed_value)
        if seed_value>=67832336:
            for seed_range in seed_ranges:
                if seed_range[0] <= seed_value < seed_range[1]:
                    print(f'Found mapping for seed={seed_value} and location={location} ')
                    return

    # Wrong Found 2322838536 in seeds at location 3642693175


if __name__ == '__main__':
    # solvePart1()
    solvePart2()
