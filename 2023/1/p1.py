def process(line):
    # find first digit
    validDigits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    # find all the digits
    digits = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            digits.append(int(line[i]))
        for j in range(3):
            if line[i : i + j + 3] in validDigits:
                digits.append(validDigits[line[i : i + j + 3]])
                # i += j + 2
                # break
        i += 1

    # get first and last digit
    number = digits[0] * 10 + digits[-1]
    print(line.strip())
    print(digits, number)
    return number


totalSum = 0
for line in open("input.txt"):
    totalSum += process(line)
print(totalSum)
