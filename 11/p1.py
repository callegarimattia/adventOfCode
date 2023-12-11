import sys
from itertools import combinations

filePath = sys.argv[1]
D = open(filePath, "r").read().split("\n")
U = [[str(x) for x in y] for y in D]


def expand(U, n):
    E = [[1 for c in range(len(U[0]))] for r in range(len(U))]
    for i in range(len(U)):
        if all(U[i][j] != "#" for j in range(len(U[i]))):
            E[i] = [n for _ in range(len(U[i]))]
    for j in range(len(U[0])):
        if all(U[i][j] != "#" for i in range(len(U))):
            for i in range(len(U)):
                E[i][j] = n
    return E


def get_galaxies(U):
    Q = []
    for i in range(len(U)):
        for j in range(len(U[i])):
            if U[i][j] == "#":
                Q.append((i, j))
    return Q


def GSD(G1, G2, E):
    D = 0
    for i in range(min(G1[0], G2[0]), max(G1[0], G2[0])):
        D += E[i][G1[1]]
    for j in range(min(G1[1], G2[1]), max(G1[1], G2[1])):
        D += E[G1[0]][j]
    return D


def solve(part2):
    E = expand(U, 1000000 if part2 else 2)
    G = get_galaxies(U)
    GP = list(combinations(G, 2))
    print(sum(GSD(x[0], x[1], E) for x in GP))


solve(False)
solve(True)
