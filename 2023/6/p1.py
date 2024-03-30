from math import sqrt, ceil, floor


def get_input():
    with open("day6/input.txt", "r") as f:
        data = f.readlines()
        times = []
        distances = []
        times = data[0].split(":")[1].split()
        distances = data[1].split(":")[1].split()
        return times, distances


def solve(time, dist):
    # DIST = HOLD * (TIME - HOLD)
    # we want HOLD * (TIME - HOLD) > DIST
    # HOLD > 0 && TIME - HOLD > 1
    # DIST > 0
    # -HOLD**2 + HOLD * TIME - DIST > 0
    if time**2 - 4 * dist < 0:
        return 0
    hold1 = (-time - sqrt(time**2 - 4 * dist)) * 0.5
    hold2 = (-time + sqrt(time**2 - 4 * dist)) * 0.5
    # calculate minHold and maxHold from hold1, hold2
    # get the next smallest integer (!= hold1) for minHold
    # # get the previous largest integer (!= hold2) for maxHold
    minHold = ceil(hold1 + 10**-4)
    maxHold = floor(hold2 - 10**-4)
    return maxHold - minHold + 1


def part1(data):
    times, distances = data
    times = [int(x) for x in times]
    distances = [int(x) for x in distances]
    runs = list(zip(times, distances))
    total = 1
    for run in runs:
        total *= solve(run[0], run[1])
    print(f"Part 1: {total}")


def part2(data):
    # squash the times and distances in one whole run
    time, dist = data
    time = int("".join(time))
    dist = int("".join(dist))
    print(f"Part 2: {solve(time, dist)}")


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
