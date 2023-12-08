import math

data = open("day8/input.txt").read().strip()
lines = data.split("\n")


# least common multiple
def lcm(nums):
    ans = 1
    for num in nums:
        ans = (num * ans) // math.gcd(num, ans)
    return ans


# parse input
GO = {"L": {}, "R": {}}
steps, rule = data.split("\n\n")
for line in rule.split("\n"):
    st, lr = line.split("=")
    st = st.strip()
    left, right = lr.split(",")
    left = left.strip()[1:].strip()
    right = right[:-1].strip()
    GO["L"][st] = left
    GO["R"][st] = right


def solve2():
    start = []
    for s in GO["L"]:
        if s.endswith("A"):
            start.append(s)
    T, t = {}, 0
    while True:
        pos = []
        for i, p in enumerate(start):
            p = GO[steps[t % len(steps)]][p]
            if p.endswith("Z"):
                T[i] = t + 1
                if len(T) == len(start):
                    return lcm(T.values())
            pos.append(p)
        start = pos
        t += 1


def solve1():
    for s in GO["L"]:
        if s.endswith("AAA"):
            start = s
    t = 0
    p = start
    while True:
        p = GO[steps[t % len(steps)]][p]
        if p.endswith("Z"):
            return t + 1
        t += 1
        start = p


print(solve1())
print(solve2())
