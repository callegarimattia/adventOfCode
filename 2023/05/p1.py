def parse_input(input_data):
    initial_values = input_data[0].split(": ")[1].split()
    for i, value in enumerate(initial_values):
        initial_values[i] = int(value)

    mappings = []
    i = -1

    for line in input_data[2:]:
        if not line:
            pass
        elif line[0].isdigit():
            mappings[i].append(line.split())

            for j, num in enumerate(mappings[i][-1]):
                mappings[i][-1][j] = int(num)

        else:
            mappings.append([])
            i += 1

    return initial_values, mappings


def find_location(n, mappings, reverse=False):
    if reverse:
        mappings = mappings[::-1]

    for map in mappings:
        for submap in map:
            if reverse:
                submap = (submap[1], submap[0], submap[2])
            if n in range(submap[1], submap[1] + submap[2]):
                n += submap[0] - submap[1]
                break
    return n


def find_in_range(start, end, initial_values, mappings, step):
    if not step:
        return end
    for location in range(start, end + 1, step):
        for s in range(0, len(initial_values), 2):
            if find_location(location, mappings, True) in range(
                initial_values[s], initial_values[s] + initial_values[s + 1]
            ):
                return find_in_range(
                    location - step, location, initial_values, mappings, step // 10
                )


def execute(input_data):
    initial_values, mappings = parse_input(input_data)

    min_value = float("inf")
    for value in initial_values:
        value = find_location(value, mappings)
        min_value = min(min_value, value)

    max_span = 0
    for i in range(0, len(initial_values), 2):
        max_span = max(max_span, initial_values[i] + initial_values[i + 1])

    step_size = 10**4
    ranged_value = find_in_range(0, max_span, initial_values, mappings, step_size)

    print(f"Part 1: {min_value}")
    print(f"Part 2: {ranged_value}")


if __name__ == "__main__":
    with open("day5/input.txt") as file:
        input_data = file.read().splitlines()
    execute(input_data)
