# up recursion limit
from sys import setrecursionlimit

setrecursionlimit(1000000)

D = open("day10/input.txt").read().split("\n")
G = [[D[i][j] for j in range(len(D[i]))] for i in range(len(D))]
S = [[0 for j in range(len(G[i]))] for i in range(len(G))]


# y x
GO = {
    "RIGHT": (0, 1),
    "LEFT": (0, -1),
    "UP": (-1, 0),
    "DOWN": (1, 0),
}
MAP = {
    "|": ["UP", "DOWN"],
    "-": ["LEFT", "RIGHT"],
    "L": ["UP", "RIGHT"],
    "J": ["UP", "LEFT"],
    "7": ["DOWN", "LEFT"],
    "F": ["DOWN", "RIGHT"],
}
FROM = {
    "RIGHT": "LEFT",
    "LEFT": "RIGHT",
    "UP": "DOWN",
    "DOWN": "UP",
}

# S is hardcoded to the corresponding pipe
PIPES = {
    "|": [["0", "#", "0"], ["0", "#", "0"], ["0", "#", "0"]],
    "-": [["0", "0", "0"], ["#", "#", "#"], ["0", "0", "0"]],
    "L": [["0", "#", "0"], ["0", "#", "#"], ["0", "0", "0"]],
    "J": [["0", "#", "0"], ["#", "#", "0"], ["0", "0", "0"]],
    "F": [["0", "0", "0"], ["0", "#", "#"], ["0", "#", "0"]],
    "7": [["0", "0", "0"], ["#", "#", "0"], ["0", "#", "0"]],
    "S": [["0", "#", "0"], ["0", "#", "#"], ["0", "0", "0"]],
    ".": [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]],
}


def dfs(G, y, x, DIS, DIR, S):
    if x < 0 or x >= len(G[0]) or y < 0 or y >= len(G):
        return
    if G[y][x] in MAP.keys():
        S[y][x] = min(S[y][x], DIS) if S[y][x] != 0 else DIS
        DIRS = MAP[G[y][x]].copy()
        if DIR in DIRS:
            DIRS.remove(DIR)
            dfs(G, y + GO[DIRS[0]][0], x + GO[DIRS[0]][1], DIS + 1, FROM[DIRS[0]], S)


def solve():
    SX, SY = -1, -1
    for i in range(len(D)):
        SX = D[i].find("S")
        if SX != -1:
            SY = i
            break
    for DIR in GO.keys():
        dfs(G, SY + GO[DIR][0], SX + GO[DIR][1], 1, FROM[DIR], S)
    max_dist = max([max(S[i]) for i in range(len(S))])
    print(max_dist)


def lay_pipe(BIG, D, S):
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] in PIPES.keys() and (S[i][j] or D[i][j] == "S"):
                for k in range(3):
                    for w in range(3):
                        BIG[i * 3 + k][j * 3 + w] = PIPES[D[i][j]][k][w]


# bfs
def flood(BIG, y, x, V, Q):
    if x < 0 or x >= len(BIG[0]) or y < 0 or y >= len(BIG) or V[y][x]:
        return
    V[y][x] = 1
    if BIG[y][x] != "#":
        for i in range(-1, 2):
            for j in range(-1, 2):
                Q.append((y + i, x + j))


def solve2():
    BIG = [[0 for j in range(len(G[0]) * 3)] for i in range(len(G) * 3)]
    lay_pipe(BIG, G, S)
    V = [[0 for j in range(len(BIG[i]))] for i in range(len(BIG))]
    Q = [
        (0, 0),
        (len(BIG) - 1, 0),
        (0, len(BIG[0]) - 1),
        (len(BIG) - 1, len(BIG[0]) - 1),
    ]
    while Q:
        y, x = Q.pop()
        flood(BIG, y, x, V, Q)
    count = 0
    for i in range(0, len(BIG), 3):
        for j in range(0, len(BIG[i]), 3):
            if BIG[i][j] != "#" and not V[i][j]:
                flag = True
                for k in range(3):
                    for w in range(3):
                        if BIG[i + k][j + w] == "#":
                            flag = False
                if flag:
                    count += 1
    print(count)


solve()
solve2()
