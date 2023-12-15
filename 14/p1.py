import sys

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
G = [[c for c in row] for row in L]


def tilt(G):
    lr, lc = len(G), len(G[0])
    for col in range(lr):
        for _ in range(lc):
            for row in range(lr):
                if G[row][col] == "O" and row > 0 and G[row - 1][col] == ".":
                    G[row][col] = "."
                    G[row - 1][col] = "O"
    return G


def rotate(G):
    # Rotate G counter-clockwise
    lr, lc = len(G), len(G[0])
    T = [["X" for _ in range(lr)] for _ in range(lc)]
    for row in range(lr):
        for col in range(lc):
            T[col][lr - row - 1] = G[row][col]
    return T


def show(G):
    for row in range(len(G)):
        print("".join(G[row]))
    print()


def load(G):
    ans = 0
    lr, lc = len(G), len(G[0])
    for row in range(lr):
        for col in range(lc):
            if G[row][col] == "O":
                ans += len(G) - row
    return ans


memo = {}


def solve(G, part2=False):
    cycles = 10**9
    if not part2:
        print(load(tilt(G)))
    else:
        cycle = 0
        while cycle < cycles:
            cycle += 1
            for j in range(4):
                G = tilt(G)
                G = rotate(G)
            print("-" * 100)
            show(G)
            print("-" * 100)
            key = tuple(tuple(row) for row in G)
            if key in memo:
                period = cycle - memo[key]
                t = (cycles - cycle) // period
                cycle += t * period
            memo[key] = cycle
        print(load(G))


solve(G)
solve(G, True)
