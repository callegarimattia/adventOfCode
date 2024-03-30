def extract_game_info(line):
    line = line.split(":")[1].strip()
    line = [lin.strip() for lin in line.split(";")]
    hints = []
    # hints are in [R, G, B] order
    for hint in line:
        hints.append([hin.strip() for hin in hint.split(",")])
    value = 0
    color = ""
    extractions = []
    for hint in hints:
        for string in hint:
            if string[1].isdigit():
                value = int(string[:2])
                color = string[3]
            else:
                value = int(string[0])
                color = string[2]
            extractions.append((value, color))
    return extractions


def is_game_possible(game):
    for hint in game:
        if hint[1] == "r":
            if hint[0] < 1 or hint[0] > 12:
                return False
        elif hint[1] == "g":
            if hint[0] < 1 or hint[0] > 13:
                return False
        elif hint[1] == "b":
            if hint[0] < 1 or hint[0] > 14:
                return False
    return True


def get_minimum_config_power(game):
    minR = 0
    minG = 0
    minB = 0
    for hint in game:
        if hint[1] == "r":
            minR = max(hint[0], minR)
        elif hint[1] == "g":
            minG = max(hint[0], minG)
        elif hint[1] == "b":
            minB = max(hint[0], minB)
    return minR * minG * minB


# parse the input
with open("input.txt", "r") as f:
    lines = f.readlines()
    games = []
    tSum = 0
    powerSet = 0
    for idx, line in enumerate(lines):
        game = extract_game_info(line)
        if is_game_possible(game):
            tSum += idx + 1
        powerSet += get_minimum_config_power(game)
    print("----------------- Part 1 -----------------")
    print("Sum of id of possible games: ", tSum)
    print("----------------- Part 2 -----------------")
    print("Power of set of minimal configurations: ", powerSet)
