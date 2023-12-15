import sys
from itertools import product

D = open(sys.argv[1]).read().split("\n\n")
D = [d.split("\n") for d in D]
D = [[[c for c in L] for L in d] for d in D]


def printP(P):
    for L in P:
        print(L)
    print()


def f(a, b):
    a = a[::-1]
    if len(a) > len(b):
        a, b = b, a
    return a == b[: len(a)]


# get column from 2d array
def getCol(P, x):
    return [P[y][x] for y in range(len(P))]


def F(P, skipC=0, skipR=0):
    col, row = 0, 0

    # check columns
    for y in range(1, len(P)):
        if (
            all(f(getCol(P, x)[:y], getCol(P, x)[y:]) for x in range(len(P[0])))
            and y != skipR
        ):
            row = y
    # check rows
    for x in range(1, len(P[0])):
        if all(f(P[y][:x], P[y][x:]) for y in range(len(P))) and x != skipC:
            col = x
    return col, row


def smudge(P, x, y):
    # smudge a point in a copy of the array
    P = [L[:] for L in P]
    P[y][x] = "." if P[y][x] == "#" else "#"
    return P


def solve(part2=False):
    ans = 0
    for P in D:
        col, row = F(P)
        if part2:
            for x, y in product(range(len(P[0])), range(len(P))):
                T = smudge(P, x, y)
                newCol, newRow = F(T, col, row)
                if newCol or newRow:
                    col, row = newCol, newRow
                    break
        ans += col + row * 100
    print(ans)


solve()
solve(True)
