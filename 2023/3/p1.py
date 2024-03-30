import re

SYMBOL_PATTERN = r"[^\d\w.]"


def is_symbol_adjacent(matrix, i, j):
    pattern = re.compile(SYMBOL_PATTERN)
    # check adjacent cells
    if i > 0:
        if pattern.match(matrix[i - 1][j]):
            return True
    if i < height - 1:
        if pattern.match(matrix[i + 1][j]):
            return True
    if j > 0:
        if pattern.match(matrix[i][j - 1]):
            return True
    if j < width - 1:
        if pattern.match(matrix[i][j + 1]):
            return True

    # check diagonal cells
    if i > 0 and j > 0:
        if pattern.match(matrix[i - 1][j - 1]):
            return True
    if i < height - 1 and j < width - 1:
        if pattern.match(matrix[i + 1][j + 1]):
            return True
    if i > 0 and j < width - 1:
        if pattern.match(matrix[i - 1][j + 1]):
            return True
    if i < height - 1 and j > 0:
        if pattern.match(matrix[i + 1][j - 1]):
            return True
    return False


def get_whole_number(matrix, i, j):
    # given a matrix and a position, return the whole number
    # that could start before the position and end after the position
    # if the position is not a digit, return None
    # delete the number from the matrix
    if not matrix[i][j].isdigit():
        return None
    num = matrix[i][j]
    start = j
    # check left until a non-digit is found or the left edge is reached
    while j > 0 and matrix[i][j - 1].isdigit():
        num = matrix[i][j - 1] + num
        j -= 1

    j = start
    # check right until a non-digit is found or the right edge is reached
    while j < width - 1 and matrix[i][j + 1].isdigit():
        num = num + matrix[i][j + 1]
        j += 1
    num = int(num)
    return num


def get_numbers_near_star(matrix, i, j):
    # return the numbers adjacent to the star
    # numbers must be separated by a non-digit
    # flags = [left, right, up, down, up-left, up-right, down-left, down-right]
    # get at most 2 numbers
    FLAGS = [False, False, False, False, False, False, False, False]
    nums = []
    if matrix[i][j] != "*":
        return None
    if i > 0:
        num = get_whole_number(matrix, i - 1, j)
        if num:
            nums.append(num)
            FLAGS[2] = True
    if i < height - 1:
        num = get_whole_number(matrix, i + 1, j)
        if num:
            nums.append(num) if num else None
            FLAGS[3] = True
    if FLAGS.count(True) == 2:
        return nums
    if j > 0:
        num = get_whole_number(matrix, i, j - 1)
        if num:
            nums.append(num) if num else None
            FLAGS[0] = True
    if j < width - 1:
        num = get_whole_number(matrix, i, j + 1)
        if num:
            nums.append(num) if num else None
            FLAGS[1] = True
    if FLAGS.count(True) == 2:
        return nums
    # check diagonals only if no adjacent numbers were found yet
    # in that direction (check up-left only if up is False, etc.)
    if i > 0 and j > 0 and not FLAGS[2]:
        num = get_whole_number(matrix, i - 1, j - 1)
        if num:
            nums.append(num) if num else None
            FLAGS[4] = True
    if i > 0 and j < width - 1 and not FLAGS[2]:
        num = get_whole_number(matrix, i - 1, j + 1)
        if num:
            nums.append(num) if num else None
            FLAGS[5] = True
    if i < height - 1 and j > 0 and not FLAGS[3]:
        num = get_whole_number(matrix, i + 1, j - 1)
        if num:
            nums.append(num) if num else None
            FLAGS[6] = True
    if i < height - 1 and j < width - 1 and not FLAGS[3]:
        num = get_whole_number(matrix, i + 1, j + 1)
        if num:
            nums.append(num) if num else None
            FLAGS[7] = True
    if FLAGS.count(True) == 2:
        return nums
    return None


# Day 3: Gear ratios
with open("day3/input.txt", "r") as f:
    text = f.read()
    lines = text.split("\n")
    width = len(lines[0])
    height = len(lines)
    # PART 1
    # tSum = 0
    # tNum = ""
    # valid = False
    # for i in range(height):
    #     for j in range(width):
    #         if lines[i][j].isdigit():
    #             tNum += lines[i][j]
    #             if is_symbol_adjacent(lines, i, j):
    #                 valid = True
    #         else:
    #             if valid:
    #                 tSum += int(tNum)
    #             tNum = ""
    #             valid = False
    #     if valid:
    #         tSum += int(tNum)
    #     tNum = ""
    #     valid = False

    tSum = 0
    # for each asterisk check if it has a two separate numbers adjacent to it
    # if so, add the number to the total sum
    for i in range(height):
        for j in range(width):
            nums = get_numbers_near_star(lines, i, j)
            if nums:
                print(nums)
                tSum += nums[0] * nums[1]
    print(tSum)
