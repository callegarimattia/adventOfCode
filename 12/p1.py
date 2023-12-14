import sys
from tqdm import tqdm

D = open(sys.argv[1]).read()
L = D.split("\n")


DP = {}


def dp(dots, pattern, i, pi, current):
    comb = (i, pi, current)
    if comb in DP:
        return DP[comb]

    if i == len(dots):
        if pi == len(pattern) and current == 0:
            return 1
        elif pi == len(pattern) - 1 and pattern[pi] == current:
            return 1
        else:
            return 0
    res = 0

    for c in [".", "#"]:
        if dots[i] == c or dots[i] == "?":
            if c == "." and current == 0:
                res += dp(dots, pattern, i + 1, pi, current)
            elif (
                c == "."
                and current > 0
                and pi < len(pattern)
                and pattern[pi] == current
            ):
                res += dp(dots, pattern, i + 1, pi + 1, 0)
            elif c == "#":
                res += dp(dots, pattern, i + 1, pi, current + 1)

    DP[comb] = res
    return res


def solve(part2=False):
    ans = 0
    for line in tqdm(L):
        dots, pattern = line.split()
        if part2:
            dots = "?".join([dots for _ in range(5)])
            pattern = ",".join([pattern for _ in range(5)])
        pattern = [int(x) for x in pattern.split(",")]
        result = dp(dots, pattern, 0, 0, 0)
        DP.clear()
        ans += result
    print(ans)


solve()
solve(True)
