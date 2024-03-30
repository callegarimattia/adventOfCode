import sys


D = open(sys.argv[1]).read().strip()
D = D.split("\n")
G = [list(row) for row in D]

GO = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
DIR = {"UP": "^", "DOWN": "v", "LEFT": "<", "RIGHT": ">"}
SPLIT = {"|": ["UP", "DOWN"], "-": ["LEFT", "RIGHT"]}
# \
REFLECT1 = {"DOWN": "RIGHT", "UP": "LEFT", "LEFT": "UP", "RIGHT": "DOWN"}
# /
REFLECT2 = {"DOWN": "LEFT", "UP": "RIGHT", "LEFT": "DOWN", "RIGHT": "UP"}


def light(G, L, r, c, dir, queue):
    if r < 0 or c < 0 or r >= len(G) or c >= len(G[0]):
        return
    if L[r][c] in DIR.values() and L[r][c] == DIR[dir]:
        return
    if G[r][c] == ".":
        L[r][c] = DIR[dir]
        queue.append((r + GO[dir][0], c + GO[dir][1], dir))
    elif G[r][c] in SPLIT.keys():
        split = SPLIT[G[r][c]]
        if dir in split:
            L[r][c] = DIR[dir]
            queue.append((r + GO[dir][0], c + GO[dir][1], dir))
        else:
            for d in split:
                L[r][c] = DIR[d]
                queue.append((r + GO[d][0], c + GO[d][1], d))
    else:
        reflect = REFLECT1 if G[r][c] == "\\" else REFLECT2
        L[r][c] = DIR[dir]
        queue.append((r + GO[reflect[dir]][0], c + GO[reflect[dir]][1], reflect[dir]))


def shine(L, q):
    while q:
        r, c, dir = q.pop()
        light(G, L, r, c, dir, q)


def energy(L):
    return sum(
        [1 for r in range(len(L)) for c in range(len(L[r])) if L[r][c] in DIR.values()]
    )


def solve():
    max_energy = 0
    for dir in DIR.keys():
        if dir == "UP" or dir == "DOWN":
            r = 0 if dir == "DOWN" else len(G) - 1
            for c in range(len(G[r])):
                L = [["." for _ in range(len(G[0]))] for _ in range(len(G))]
                shine(L, [(r, c, dir)])
                max_energy = max(max_energy, energy(L))
        else:
            c = 0 if dir == "RIGHT" else len(G[0]) - 1
            for r in range(len(G)):
                L = [["." for _ in range(len(G[0]))] for _ in range(len(G))]
                shine(L, [(r, c, dir)])
                if r == 0 and c == 0 and dir == "RIGHT":
                    print(energy(L))
                max_energy = max(max_energy, energy(L))
    print(max_energy)


solve()
