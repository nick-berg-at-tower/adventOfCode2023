# Test
# Time:      7  15   30
# Distance:  9  40  200
# Race 1 2-5 = 4
# Race 2 4-11 = 8
# Race 3 11-19 = 9

def distance_travelled(total_time, button_time):
    return (total_time-button_time)*button_time


def solve_race(total_time, record_distance):
    winning_button_times = []
    for button_time in range(0, total_time):
        race_distance_travelled = distance_travelled(total_time, button_time)
        if race_distance_travelled>record_distance:
            winning_button_times.append(button_time)
    return len(winning_button_times)

def solvePart1():
    race1 = solve_race(7,9)
    race2 = solve_race(15, 40)
    race3 = solve_race(30,200)
    print(f'Test Solution = {race1*race2*race3}')

    race1 = solve_race(47, 207)
    race2 = solve_race(84, 1394)
    race3 = solve_race(74, 1209)
    race4 = solve_race(67, 1014)
    print(f'Real Solution = {race1 * race2 * race3 * race4}')

#     The minimum seed is 111959634 at 322500873



def solvePart2():
    print(f'Test Solution = {solve_race(71530, 940200)}')
    print(f'Real Solution = {solve_race(47847467, 207139412091014)}')


if __name__ == '__main__':
    # solvePart1()
    solvePart2()

