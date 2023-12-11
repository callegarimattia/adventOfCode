def line_to_lists(line):
    # get list of winning numbers after ":" and before "|"
    winning = line.split(":")[1].split("|")[0].strip().split(" ")
    guesses = line.split("|")[1].strip().split(" ")
    # remove empty strings
    winning = list(filter(None, winning))
    guesses = list(filter(None, guesses))
    return winning, guesses


def get_points(winning, guesses):
    # count for each line how many winning numbers are in the guesses
    # each number doubles the points (first number 1 point, second 2 points, etc.)
    count = 0
    points = 0
    for number in winning:
        if number in guesses:
            count += 1
    points += pow(2, count - 1) if count else 0
    return points


def get_count(winning, guesses):
    # count for each line how many winning numbers are in the guesses
    # each number doubles the points (first number 1 point, second 2 points, etc.)
    count = 0
    for number in winning:
        if number in guesses:
            count += 1
    return count


# PART 1
# with open("day4/input.txt", "r") as f:
#     prize = 0
#     for line in f:
#         winning, guesses = line_to_lists(line)
#         # count for each line how many winning numbers are in the guesses
#         # each number doubles the points (first number 1 point, second 2 points, etc.)
#         points = get_points(winning, guesses)
#         prize += points
#     print(prize)

# PART 2
# each number now gives a copy of the next card down the line
# i.e 2 points -> copies of the next two cards
# 3 points -> copies of the next three cards
# etc.
# good idea to keep track of the wins for each line
# and then multiply the wins with the number of points
# traversing the list backwards
with open("day4/input.txt", "r") as f:
    instances = [1 for line in f]
    f.seek(0)
    points = [get_count(*line_to_lists(line)) for line in f]
    print(points)
    # calculate the copies for each line
    # each card gives a copy of the next-[points] cards
    # i.e. 2 points -> copies of the next two cards
    # 3 points -> copies of the next three cards
    # etc.
    # travese the list and add instances to the next [points] cards
    # if the points go over the length of the list, discard the rest
    for i in range(len(instances)):
        for j in range(points[i]):
            if i + j < len(instances) - 1:
                instances[i + j + 1] += instances[i]
    print(instances)
    print(sum(instances))
